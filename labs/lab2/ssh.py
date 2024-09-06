import boto3

# Initialize EC2 client
client = boto3.client('ec2')

response = client.authorize_security_group_ingress(
    CidrIp='0.0.0.0/0',
    FromPort=22,
    # GroupId='string',
    GroupName='22756463-sg',
    IpProtocol='tcp',
    ToPort=22,
)

print(f'Security Group Ingress successfully set {response}')