import boto3

# Initialize EC2 client
client = boto3.client('ec2')

response = client.create_security_group(
    Description='security group for development environment',
    GroupName='22756463-sg',
    TagSpecifications=[
        {
            'ResourceType': 'security-group',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': '22756463'
                },
            ]
        },
    ],
)

print(response)