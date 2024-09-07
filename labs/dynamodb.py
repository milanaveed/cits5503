import boto3
from botocore.exceptions import ClientError
import os

# Initialise clients for DynamoDB and S3
dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
s3 = boto3.client('s3')

# Define the S3 bucket name
BUCKET_NAME = '22756463-cloudstorage'
# Define the DynamoDB table name
TABLE_NAME = 'CloudFiles'

# Create the DynamoDB table
def create_cloudfiles_table():
    # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/create_table.html
    try:
        table = dynamodb.create_table(
            TableName=TABLE_NAME,
            KeySchema=[
                {'AttributeName': 'userId', 'KeyType': 'HASH'},  # Partition key
                {'AttributeName': 'fileName', 'KeyType': 'RANGE'},  # Sort key
            ],
            AttributeDefinitions=[
                {'AttributeName': 'userId', 'AttributeType': 'S'},  # String type
                {'AttributeName': 'fileName', 'AttributeType': 'S'},  # String type
            ],
            ProvisionedThroughput={'ReadCapacityUnits': 10, 'WriteCapacityUnits': 10}
        )
        print(f"Creating table {TABLE_NAME}. Please wait...")
        table.meta.client.get_waiter('table_exists').wait(TableName=TABLE_NAME)
        print(f"Table {TABLE_NAME} created successfully.")
        return table
    except ClientError as e:
        if e.response['Error']['Code'] == 'ResourceInUseException':
            print(f"Table {TABLE_NAME} already exists.")
        else:
            raise

# Get the attributes for each file in the S3 bucket, including ACL information
def get_s3_file_attributes(bucket_name):
    try:
        # List all files in the S3 bucket
        response = s3.list_objects_v2(Bucket=bucket_name)

        if 'Contents' not in response:
            print(f"No files found in bucket {bucket_name}.")
            return []

        files = []
        # Iterate through each file in the bucket
        for object in response['Contents']:
            s3_key = object['Key']

            # Get the ACL (Access Control List) for the file
            acl_response = s3.get_object_acl(Bucket=bucket_name, Key=s3_key)
            userId = acl_response['Owner']['ID']
            owner = acl_response['Owner']['DisplayName']
            permission = acl_response['Grants'][0]['Permission']

            # Construct the file attributes
            file_info = {
                'userId': userId, 
                'fileName': s3_key.split('/')[-1],
                'path': s3_key,
                'lastUpdated': object['LastModified'].isoformat(),
                'owner': owner,  
                'permissions': permission  
            }
            files.append(file_info)
        return files

    except ClientError as e:
        print(f"Error accessing S3 bucket: {e}")
        return []

# Write file attributes to DynamoDB
def write_to_dynamodb(table_name, files):
    table = dynamodb.Table(table_name)

    for file_info in files:
        try:
            # Insert the file attributes as a new item in the DynamoDB table
            table.put_item(Item=file_info)
            print(f"Successfully inserted: {file_info['fileName']}")
        except ClientError as e:
            print(f"Error inserting {file_info['fileName']} into DynamoDB: {e.response['Error']['Message']}")

# Main function
if __name__ == "__main__":
    # Step 1: Create the table
    create_cloudfiles_table()

    # Step 2: Get file attributes from S3
    files = get_s3_file_attributes(BUCKET_NAME)

    # Step 3: Write the attributes to DynamoDB
    if files:
        write_to_dynamodb(TABLE_NAME, files)
        print("Done.")
    else:
        print("No files to insert.")