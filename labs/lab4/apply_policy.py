import boto3
import json

# Initialise the S3 client
s3 = boto3.client('s3')

bucket_name = '22756463-cloudstorage' 
student_number = '22756463'

# Define the bucket policy
bucket_policy = {
    "Version": "2012-10-17",
    "Statement": [{
        "Sid": "AllowAllS3ActionsInUserFolderForUserOnly",
        "Effect": "Deny",
        "Principal": "*",
        "Action": "s3:*",
        "Resource": f"arn:aws:s3:::{bucket_name}",
        "Condition": {
            "StringNotLike": {
                "aws:username": f"{student_number}@student.uwa.edu.au"
            }
        }
    }]
}

# Convert the policy from dictionary to JSON format
bucket_policy_json = json.dumps(bucket_policy)

# Apply the policy to the S3 bucket
def apply_bucket_policy(bucket_name, bucket_policy_json):
    try:
        # Set the bucket policy
        s3.put_bucket_policy(Bucket=bucket_name, Policy=bucket_policy_json)
        print(f"Policy applied successfully to bucket {bucket_name}")
    except Exception as e:
        print(f"Error applying policy: {e}")

if __name__ == "__main__":
    # Call the function to apply the policy
    apply_bucket_policy(bucket_name, bucket_policy_json)
