import boto3

# Initialize EC2 client
client = boto3.client('ec2')

response = client.create_key_pair(
    KeyName='22756463-key',
    # DryRun=True|False,
    # KeyType='rsa'|'ed25519',
    TagSpecifications=[
        {
            'ResourceType': 'key-pair',
            # 'Tags': [
            #     {
            #         'Key': 'Name',
            #         'Value': '22756463'
            #     },
            # ]
        },
    ],
    KeyFormat='pem'|'ppk'
)

print(response.get('KeyMaterial'))
print(response.get('KeyFingerprint'))