<div style="text-align: center;">

  <h1>Labs 6-9</h1>
  
  <p>Student ID: 22756463</p>
  <p>Student Name: Mila (Yue) Zhang</p>

</div>

<div style="page-break-after: always;"></div>

# Lab 6

## Set up an EC2 instance

### [1] Create an EC2 micro instance with Ubuntu and SSH into it. 

#### 1.1 Create an EC2 micro instance

##### Python script `create_ec2_instance.py`
```python
import boto3
from botocore.exceptions import ClientError

# Create a Boto3 EC2 client to interact with AWS EC2 service
ec2 = boto3.client('ec2')

# Function to create an EC2 instance
def create_instance(key_name, security_group_name, ami_id):
    try:
        # Create the EC2 instance using run_instances API call
        # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/run_instances.html
        instance = ec2.run_instances(
            ImageId= ami_id,                  # AMI ID for the EC2 instance (Ubuntu or other OS)
            MinCount=1,                       # Minimum number of instances to create (1 in this case)
            MaxCount=1,                       # Maximum number of instances to create (1 in this case)
            InstanceType='t2.micro',           # Instance type (t2.micro for free tier)
            KeyName=key_name,                 # Name of the SSH key pair for access
            SecurityGroups=[security_group_name],  # Security group to associate with the instance
            TagSpecifications=[               # Adding a tag to the instance (for identification)
                    {
                        'ResourceType': 'instance',
                        'Tags': [
                            {'Key': 'Name', 'Value': f'22756463-vm'}  # Tag with a key-value pair for Name
                        ]
                    }
                ]
        )
        # Extract the instance ID from the response
        instance_id = instance['Instances'][0]['InstanceId']
        print(f"EC2 instance created with Instance ID: {instance_id}")
        return instance_id  # Return the instance ID
    except ClientError as e:
        # Print an error message if the instance creation fails
        print(f"Error creating EC2 instance: {e}")
        return None  # Return None in case of an error

# Main function to set up instance creation
def main():
    sg_name = "22756463-sg"  # Security group name
    sg_description = "security group for development environment"  # Security group description
    key_name = "22756463-key"  # SSH key pair name
    ami_id = "ami-0a0e5d9c7acc336f1"  # AMI ID for the instance (replace with appropriate AMI for your region)
    
    # Create an EC2 instance using the create_instance function
    instance_id = create_instance(key_name, sg_name, ami_id)

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
```
A detailed explanation is provided as comments in the code block above.

##### Results
Created an EC2 instance with name `22756463-vm` and ID `i-01b55b25eb0b60503`.
![alt text](image-42.png)

#### 1.2 SSH into the EC2 instance
I obtained the public IP address of the EC2 instances from the AWS console. The address is `54.152.128.37`. Then I ssh to the instance using command `ssh -i 22756463-key.pem ubuntu@54.152.128.37`.

##### Commands
- `ssh`: This is the command used to establish a secure connection to a remote machine. It uses an encrypted connection, providing a secure way to access remote servers over insecure networks.
- `-i 22756463-key.pem`:
    - `-i`: This option specifies the identity file (or private key) to use for authentication. SSH uses this key to log into the remote server without needing a password.
    - `22756463-key.pem`: This is the path to the private key file that I generated when creating the EC2 key pair. This file must have read-only permissions (chmod 400 22756463-key.pem) to ensure it is secure.
- `ubuntu`: This is the username used to log into the server. For Ubuntu AMIs, the default username is ubuntu.

##### Results
![alt text](image-43.png)

### [2] Install the Python 3 virtual environment package. 
I installed the Python3 virtual environment package by using command `sudo apt-get update`, `sudo apt-get upgrade` and `sudo apt-get install python3-venv`.

#### Commands

#### Results


### [3] Access a directory 

[Refer to the marking rubrics for sufficient step-by-step description.]

### [4] Set up a virtual environment

[Refer to the marking rubrics for sufficient step-by-step description.]

### [5] Activate the virtual environment

[Refer to the marking rubrics for sufficient step-by-step description.]

### [6] Install nginx

[Refer to the marking rubrics for sufficient step-by-step description.]

### [7] Configure nginx

[Refer to the marking rubrics for sufficient step-by-step description.]

### [8] Restart nginx

[Refer to the marking rubrics for sufficient step-by-step description.]

### [9] Access your EC2 instance

[Refer to the marking rubrics for sufficient step-by-step description.]

## Set up Django inside the created EC2 instance

### [1] Edit the following files (create them if not exist)

[Refer to the marking rubrics for sufficient step-by-step description.]

### [2] Run the web server again

[Refer to the marking rubrics for sufficient step-by-step description.]

### [3] Access the EC2 instance

[Refer to the marking rubrics for sufficient step-by-step description.]

## Set up an ALB

### [1] Create an application load balancer

[Refer to the marking rubrics for sufficient step-by-step description.]

### [2] Health check

[Refer to the marking rubrics for sufficient step-by-step description.]

### [3] Access

[Refer to the marking rubrics for sufficient step-by-step description.]

<div style="page-break-after: always;"></div>

# Lab 7

<div style="page-break-after: always;"></div>

# Lab 8

<div style="page-break-after: always;"></div>

# Lab 9

