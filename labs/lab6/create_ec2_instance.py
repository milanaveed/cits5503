import boto3
from botocore.exceptions import ClientError

# Create a Boto3 EC2 client
ec2 = boto3.client('ec2')

def create_instance(key_name, security_group_name, ami_id):
    try:
        # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/run_instances.html
        instance = ec2.run_instances(
            ImageId= ami_id,
            MinCount=1,
            MaxCount=1,
            InstanceType='t2.micro',
            KeyName=key_name,
            SecurityGroups=[security_group_name],
            TagSpecifications=[
                    {
                        'ResourceType': 'instance',
                        'Tags': [
                            {'Key': 'Name', 'Value': f'22756463-vm'}
                        ]
                    }
                ]
        )
        instance_id = instance['Instances'][0]['InstanceId']
        print(f"EC2 instance created with Instance ID: {instance_id}")
        return instance_id
    except ClientError as e:
        print(f"Error creating EC2 instance: {e}")
        return None
    
def main():
    sg_name = "22756463-sg"
    sg_description = "security group for development environment"
    key_name = "22756463-key"
    ami_id = "ami-0a0e5d9c7acc336f1"
    
    # Create an EC2 instance
    instance_id = create_instance(key_name, sg_name, ami_id)

if __name__ == "__main__":
    main()