import boto3
from botocore.exceptions import ClientError

# Initialize EC2 client
ec2 = boto3.client('ec2')

# Step 1: Create a security group
def create_security_group(group_name, description):
    try:
        # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_security_group.html
        response = ec2.create_security_group(
            GroupName=group_name,
            Description=description,
        )
        security_group_id = response['GroupId']
        print(f'Security Group {group_name} created with ID: {security_group_id}')
        return security_group_id
    except ClientError as e:
        print(f"Error creating security group: {e}")
        return None

# Step 2: Authorise inbound traffic for SSH
def authorize_security_group_ingress(group_name):
    try:
        # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/authorize_security_group_ingress.html
        ec2.authorize_security_group_ingress(
            GroupName= group_name,
            # CidrIp='0.0.0.0/0',
            # GroupId=group_id,
            IpPermissions=[
                {
                    'IpProtocol': 'tcp',
                    'FromPort': 22,
                    'ToPort': 22,
                    'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
                }
            ]
        )
        print(f"SSH rule added to Security Group: {group_name}")
    except ClientError as e:
        print(f"Error adding SSH rule to security group: {e}")

# Step 3: Create a key pair
def create_key_pair(key_name):
    try:
        # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_key_pair.html
        key_pair = ec2.create_key_pair(KeyName=key_name)
        private_key = key_pair['KeyMaterial']
        
        # Save the private key to a .pem file
        with open(f"{key_name}.pem", "w") as key_file:
            key_file.write(private_key)
        
        print(f"Key pair {key_name} created and saved as {key_name}.pem")

    except ClientError as e:
        print(f"Error creating key pair: {e}")

# Step 4: Create the EC2 instance
def create_instance(key_name, security_group_name, ami_id):
    try:
        # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/run_instances.html
        instances = ec2.run_instances(
            ImageId= ami_id,
            MinCount=1,
            MaxCount=1,
            InstanceType='t2.micro',
            KeyName=key_name,
            SecurityGroups=[security_group_name],
            # SecurityGroupIds=[security_group_id],
        )
        instance_id = instances['Instances'][0]['InstanceId']
        print(f"EC2 instance created with Instance ID: {instance_id}")
        return instance_id
    except ClientError as e:
        print(f"Error creating EC2 instance: {e}")
        return None

# Step 5: Add a tag to the instance
def add_tag(instance_id, tag_key, tag_value):
    try:
        # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_tags.html
        ec2.create_tags(
            Resources=[instance_id],
            Tags=[
                {'Key': tag_key, 'Value': tag_value}
            ]
        )
        print(f"Tag '{tag_key}: {tag_value}' added to instance {instance_id}")
    except ClientError as e:
        print(f"Error tagging instance: {e}")

# Step 6: Get the public IP address of the instance
def get_public_ip(instance_id):
    try:
        # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_instances.html
        reservations = ec2.describe_instances(InstanceIds=[instance_id])
        public_ip = reservations['Reservations'][0]['Instances'][0]['PublicIpAddress']
        print(f"Public IP address of the instance: {public_ip}")
        return public_ip
    except ClientError as e:
        print(f"Error retrieving public IP: {e}")
        return None

# Main function to run the script
def main():
    sg_name = "22756463-sg3"
    sg_description = "security group for development environment"
    key_name = "22756463-key3"
    tag_key = "Name"
    tag_value = "22756463-3"
    ami_id = "ami-0a0e5d9c7acc336f1"
    
    # 1. Create a security group
    security_group_id = create_security_group(sg_name, sg_description)

    if security_group_id:
        # 2. Authorize inbound traffic for SSH
        authorize_security_group_ingress(sg_name)

        # 3. Create a key pair
        create_key_pair(key_name)

        # 4. Create the EC2 instance
        instance_id = create_instance(key_name, sg_name, ami_id)

        if instance_id:
            # 5. Add a tag to the instance
            add_tag(instance_id, tag_key, tag_value)

            # 6. Get the public IP address
            get_public_ip(instance_id)

if __name__ == "__main__":
    main()
