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
I installed the Python3 virtual environment package by using command `sudo apt-get update`, `sudo apt-get upgrade` and `sudo apt-get install python3-venv`. Then I started a new Bash shell with root privileges.

#### Commands
- `sudo`: Run with elevated (root) privilege.
- `apt-get`: Package manager to install, update, upgrade and remove software packages.
- `update`: Update the package lists for my Ubuntu system. It ensures that the system is aware of the latest versions of available software and their dependencies.
- `upgrade`: The upgrade option installs the newest versions of all currently installed packages that have an available update.
- `install`: The install option tells apt-get to install the specified package or software.
- `python3-venv`: This is the package that provides the venv module for Python 3, allowing us to create and manage virtual environments in Python.
- `sudo bash`: Start a new Bash shell with root privileges.

#### Results
Updated the package lists, upgraded installed packages and installed the `venv` package.
![alt text](image-44.png)

Started a new Bash shell with root privileges.
![alt text](image-45.png)

### [3] Access a directory 
I created a directory with a path `/opt/wwc/mysites` using command `mkdir -p /opt/wwc/mysites`. I changed to the new directory by using command `cd /opt/wwc/mysites`.

#### Commands
- `mkdir`: The command to create a directory.
- `-p`: This option creates parent directories as needed. In this case, it will create /opt/wwc/ if it doesn't already exist, and then create `mysites` inside it.
- `cd`: The command to navigate into it the target directory.

#### Results
Created the target directory and changed into the directory:
![alt text](image-46.png)

### [4] Set up a virtual environment
I created a new virtual environment by using command `python3 -m venv myvenv`.

#### Commands
- `python3`:
This invokes the Python 3 interpreter.
- `-m venv`:
    - `-m` tells Python to run the `venv` module as a script, which is used to create virtual environments.
    - `venv` is a Python module used for creating virtual environments. Virtual environments allow you to manage dependencies separately from the global Python installation, which is useful for avoiding conflicts between packages in different projects.
- `myvenv`: The name of the directory where the virtual environment will be created. Once the environment is created, this directory will contain its own bin (or Scripts on Windows) folder with Python executables and a lib folder for installed packages.

#### Results
Created a new virtual environment called `myenv`.

### [5] Activate the virtual environment

#### 5.1 Activate the virtual environment
I activated a Python virtual environment that I have created with python3 -m venv by using the command `source myvenv/bin/activate`.

##### Commands
- `source`:
This is a shell command that runs the script passed to it *in the current shell session*. It allows me to execute a script without creating a new shell process, which is necessary for setting environment variables, like those used in a virtual environment.
- `myvenv/bin/activate`:
This refers to the *activation script* located in the bin directory of my virtual environment (myvenv in this case). This script modifies my shell's environment so that it uses the Python and package installations inside the virtual environment.

##### Results
Activated the virtual environment.
![alt text](image-47.png)

#### 5.2 Install Django
I installed Django, a popular web framework for Python, in my current activated virtual environment by using the command `pip install django`.

##### Commands
- `pip`: The Python package installer. It allows me to install Python libraries and frameworks.
- `install`: The install command tells pip to install a specific package.
- `django`: The name of the package to install. In this case, it refers to the Django framework, which includes everything needed to create web applications with Python.

##### Results
Installed Django.
![alt text](image-48.png)

#### 5.3 Create a Django project
I created a new Django project called lab by using the command `django-admin startproject lab`. This command initializes a new Django project directory with the basic structure and files needed to get started.

##### Commands
- `django-admin`: A command-line utility provided by Django. It is used to perform various Django-related tasks, such as starting a project, running the server, creating apps, and more.
- `startproject`: This subcommand creates a new Django project. It sets up the necessary directories and files to begin development.
- `lab`:
This is the name of the project I want to create. In this case, the project will be called lab. Django will create a directory named lab containing the initial project files.

##### Results
Created a new Django project called `lab`.

#### 5.4 Change into the Django project directory
I changed my current working directory to the `lab` directory by using command `cd lab`.

##### Commands
- `cd`: This stands for "change directory". It’s a command used to navigate between directories in my terminal or command line.
- `lab`: The name of the directory I want to navigate to.

##### Results
Changed into the directory called `lab`.
![alt text](image-49.png)

#### 5.5 Create a Django app
I created a new Django app called `polls` within my Django project by using the command `python3 manage.py startapp polls`. Django apps are components of a project that encapsulate specific functionality, making it easier to manage and reuse code.

##### Commands
- python3: This runs the Python 3 interpreter.
- `manage.py`:
This is a utility script automatically created in my Django project. It allows me to interact with my project in various ways, such as running the server, creating apps, applying migrations, and more.
- `startapp`: A Django management command used to create a new app within the project.
- `polls`: The name of the app I am creating. Django will generate a directory named polls with the necessary structure for an app.

##### Results
Created a Django app.

#### 5.6 Inspect the Django project directory structure
I looked at the files that have been created in the project direcotry by using the command `ls -R`.

##### Commands
- `ls`: This command lists the contents of the current directory.
- `-R`: It stands for recursive, meaning it will list not only the files in the current directory but also in all subdirectories.

##### Results

![alt text](image-51.png)
```
lab/                     # Main project directory
    manage.py            # Utility for interacting with the project
    lab/                 # Inner project directory (contains project settings)
        __init__.py      # Marks this directory as a Python package
        settings.py      # Configuration file for the project (database, apps, etc.)
        urls.py          # Project-level URL routing
        asgi.py          # ASGI configuration for asynchronous web requests
        wsgi.py          # WSGI configuration for web servers (e.g., Gunicorn)
    polls/               # Newly created app (based on 'startapp polls' command)
        __init__.py      # Marks the directory as a Python package
        admin.py         # Admin site configuration for managing models
        apps.py          # App configuration
        migrations/      # Directory for database migrations
            __init__.py
        models.py        # Define data models here (database tables)
        tests.py         # Write unit tests for the app
        views.py         # Handles the logic and request/response cycle
```

### [6] Install nginx
I installed the Nginx web server on Ubuntu by using the command `apt install nginx`. Nginx is a powerful, open-source HTTP and reverse proxy server, known for its high performance and low resource usage.

#### Commands
- `apt`: The package management command used in Ubuntu for installing, updating, and removing software.
- `install`: This option tells apt to install the specified package.
- `nginx`: The name of the package I want to install, which in this case is the Nginx web server.

#### Results
Installed Nginx.

### [7] Configure nginx
I edited the `/etc/nginx/sites-enabled/default` by using the command `nano /etc/nginx/sites-enabled/default`.

#### Commands
- `nano`: The text editor I am using.
- `/etc/nginx/sites-enabled/default`: The full path to the Nginx configuration file I want to edit.

#### Results
Replaced the file content:
![alt text](image-52.png)


### [8] Restart nginx
I restarted the Nginx web server on my system by using the command `service nginx restart`. Restarting Nginx is necessary after making configuration changes (such as editing the /etc/nginx/sites-enabled/default file) to apply those changes.

#### Commands
- `service`: This is the command used to manage system services (like starting, stopping, or restarting services) in many Linux distributions.
- `nginx`: This is the name of the service I am interacting with, which in this case is the Nginx web server.
- `restart`: This tells the system to stop and then start the Nginx service again, applying any new configurations.

#### Results
Restarted the Nginx web server.

### [9] Access your EC2 instance
I started the Django development server on port 8000 by using the command `python3 manage.py runserver 8000`. This is typically done during development to test the Django application locally. Then I opened the browser and entered the IP address (http://54.152.128.37/) of my EC2 instance.

#### Commands
- `python3`: This runs the Python 3 interpreter.
- `manage.py`: This is a Django utility script automatically generated when creating a Django project. It is used to perform various administrative tasks for the project, such as running the development server, creating migrations, or managing the database.
- `runserver`: This is the command that starts the Django development web server. By default, Django runs the server on port 8000, but we can specify a different port if needed.
- `8000`: This specifies the port number on which the server will listen.

#### Results
The server run as follows.
![alt text](image-53.png)

## Set up Django inside the created EC2 instance

### [1] Edit the following files (create them if not exist)
I edited files `polls/views.py`, `polls/urls.py` and `lab/urls.py` by using the command `nano`.

#### Commands
- `nano`: The text editor commonly used in Linux.

#### Results
I replaced content in those files with those provided in the lab description.
![alt text](image-55.png)
![alt text](image-56.png)
![alt text](image-57.png)

### [2] Run the web server again
I started the Django development server on port 8000 again by using the command `python3 manage.py runserver 8000`. This is typically done during development to test the Django application locally. 

#### Commands
- `python3`: This runs the Python 3 interpreter.
- `manage.py`: This is a Django utility script automatically generated when creating a Django project. It is used to perform various administrative tasks for the project, such as running the development server, creating migrations, or managing the database.
- `runserver`: This is the command that starts the Django development web server. By default, Django runs the server on port 8000, but we can specify a different port if needed.
- `8000`: This specifies the port number on which the server will listen.

#### Results
The server run as follows.
![alt text](image-53.png)


### [3] Access the EC2 instance
I accessed the EC2 instance by opening the URL `http://54.152.128.37/polls/` in a browser.

#### Results
(Zoomed in)
![alt text](image-54.png)

## Set up an ALB

### [1] Create an application load balancer
I created an application load balancer for the EC2 instance using the below Python script. I specified the region and subnet where my EC2 instance resided. Next, I created a listener for the Application Load Balancer with the default rule using Protocol: HTTP and Port 80 forwarding. I then chose the security group that allowed HTTP traffic on port 80. Finally, I added my EC2 instance as a registered target within the target group, enabling the load balancer to forward traffic to it.

#### Python script
```python
import boto3
from botocore.exceptions import ClientError

# Create a Boto3 EC2 and ELBv2 client
# ec2 client is used for interacting with EC2 instances and subnets
# elbv2 client is used for interacting with Application Load Balancer (ALB) and Target Groups
ec2 = boto3.client('ec2')
elbv2 = boto3.client('elbv2')

# Function to get available subnets in the region
def get_subnets():
    # Describe subnets in the EC2 environment
    subnets_response = ec2.describe_subnets()
    subnets = subnets_response['Subnets']
    
    # Filter subnets to only include those that are in the 'available' state
    available_subnets = [subnet for subnet in subnets if subnet['State'] == 'available']
    
    # If fewer than 2 available subnets are found, raise an exception
    if len(available_subnets) < 2:
        raise Exception('Less than 2 available subnets in this region.')
    
    return available_subnets

# Function to create an Application Load Balancer (ALB)
def create_load_balancer(sg_id, subnets):
    try:
        # Create the load balancer with the given security group and subnets
        response = elbv2.create_load_balancer(
            Name='22756463-load-balancer1',  # The name of the load balancer
            Subnets=subnets,  # Subnets where the load balancer will reside
            SecurityGroups=[sg_id],  # Security group to apply
            Scheme='internet-facing',  # Public-facing ALB
            Type='application',  # Application Load Balancer (ALB)
            IpAddressType='ipv4'  # Use IPv4
        )
        lb_arn = response['LoadBalancers'][0]['LoadBalancerArn']  # ARN (Amazon Resource Name) of the created LB
        print(f"Load Balancer created with ARN: {lb_arn}")
        return lb_arn  # Return the ARN of the load balancer
    except ClientError as e:
        print(f"Error creating load balancer: {e}")  # Catch and print errors if any
        return None

# Function to create a Target Group
def create_target_group(vpc_id):
    try:
        # Create a target group in the specified VPC
        response = elbv2.create_target_group(
            Name='22756463-target-group1',  # Name of the target group
            Protocol='HTTP',  # Protocol to use (HTTP)
            Port=80,  # Port to forward traffic (port 80)
            VpcId=vpc_id,  # VPC ID where the target group resides
            HealthCheckProtocol='HTTP',  # Health check using HTTP
            HealthCheckPort='80',  # Port to use for health checks (port 80)
            TargetType='instance'  # Target type is EC2 instances
        )
        target_group_arn = response['TargetGroups'][0]['TargetGroupArn']  # ARN of the created target group
        print(f"Target group created with ARN: {target_group_arn}")
        return target_group_arn  # Return the ARN of the target group
    except ClientError as e:
        print(f"Error creating target group: {e}")  # Catch and print errors if any
        return None

# Function to register EC2 instances with the target group
def register_targets(target_group_arn, instance_ids):
    try:
        # Prepare the list of instance IDs as target objects
        targets = [{'Id': instance_id} for instance_id in instance_ids]
        # Register the EC2 instances as targets for the target group
        elbv2.register_targets(
            TargetGroupArn=target_group_arn,  # The ARN of the target group
            Targets=targets  # EC2 instances to register
        )
        print(f"Registered instances {instance_ids} to the target group.")  # Print confirmation
    except ClientError as e:
        print(f"Error registering targets: {e}")  # Catch and print errors if any

# Function to create a listener for the load balancer
def create_listener(lb_arn, target_group_arn):
    try:
        # Create a listener for the load balancer to forward HTTP traffic to the target group
        elbv2.create_listener(
            LoadBalancerArn=lb_arn,  # ARN of the load balancer
            Protocol='HTTP',  # Protocol to use (HTTP)
            Port=80,  # Port to listen on (port 80)
            DefaultActions=[{
                'Type': 'forward',
                'TargetGroupArn': target_group_arn  # Forward traffic to the target group
            }]
        )
        print(f"Listener created for Load Balancer {lb_arn}")  # Print confirmation
    except ClientError as e:
        print(f"Error creating listener: {e}")  # Catch and print errors if any

# Main function to coordinate the creation of the ALB and associated resources
def main():
    instance_id = ['i-01b55b25eb0b60503']  # List of EC2 instance IDs to register in the target group
    sg_id = 'sg-045eebb087d4f0e9f'  # Security group ID

    # Get VPC information (first available VPC)
    vpcs = ec2.describe_vpcs()
    vpc_id = vpcs['Vpcs'][0]['VpcId']  # Extract the VPC ID
    
    # Get subnets in the VPC
    subnets = get_subnets()
    subnet_id = [subnets[0]['SubnetId'], subnets[1]['SubnetId']]  # Select two available subnets
    
    # Create the Application Load Balancer
    lb_arn = create_load_balancer(sg_id, subnet_id)

    # Create a target group within the VPC
    target_group_arn = create_target_group(vpc_id)

    # Register the EC2 instance to the target group
    register_targets(target_group_arn, instance_id)

    # Create a listener for the load balancer to forward traffic to the target group
    create_listener(lb_arn, target_group_arn)

# Entry point for the script
if __name__ == "__main__":
    main()
```
A detailed explanation is provided as comments in the code block above.

#### Results
Created an application load balancer. (I forgot to make a screenshot initially, so I created another one named "22756463-load-balancer4")
![alt text](image-60.png)

### [2] Health check
I updated the above code in Step 1 to add a health check for the target group. I specified `/polls/` as the path for the health check in the target group configuration. I then confirmed that the health check was fetching the `/polls/` page every 30 seconds as expected using AWS Console.

#### Python script 
```python
import boto3
from botocore.exceptions import ClientError

# Create a Boto3 EC2 and ELBv2 client to interact with AWS services
ec2 = boto3.client('ec2')  # EC2 client to handle EC2 and VPC-related operations
elbv2 = boto3.client('elbv2')  # ELBv2 client to manage load balancers and target groups

# Function to retrieve available subnets in the region
def get_subnets():
    # Fetch the details of all subnets in the current region
    subnets_response = ec2.describe_subnets()
    subnets = subnets_response['Subnets']
    
    # Filter only subnets that are in the 'available' state
    available_subnets = [subnet for subnet in subnets if subnet['State'] == 'available']
    
    # Ensure that there are at least 2 available subnets
    if len(available_subnets) < 2:
        raise Exception('Less than 2 available subnets in this region.')
    
    return available_subnets  # Return the list of available subnets

# Function to create a new Application Load Balancer (ALB)
def create_load_balancer(sg_id, subnets):
    try:
        # Create the load balancer with specified security groups and subnets
        response = elbv2.create_load_balancer(
            Name='22756463-load-balancer3',  # Name of the load balancer
            Subnets=subnets,  # List of subnet IDs
            SecurityGroups=[sg_id],  # Security group for the load balancer
            Scheme='internet-facing',  # Internet-facing load balancer
            Type='application',  # Type is 'application' (ALB)
            IpAddressType='ipv4'  # Use IPv4 for IP addressing
        )
        # Get the Load Balancer ARN from the response
        lb_arn = response['LoadBalancers'][0]['LoadBalancerArn']
        print(f"Load Balancer created with ARN: {lb_arn}")  # Print the ARN
        return lb_arn  # Return the ARN of the created load balancer
    except ClientError as e:
        print(f"Error creating load balancer: {e}")  # Print error message in case of failure
        return None  # Return None if creation fails

# Function to create a target group within a VPC
def create_target_group(vpc_id):
    try:
        # Create a target group for the load balancer, with HTTP health check on /polls/
        response = elbv2.create_target_group(
            Name='22756463-target-group3',  # Name of the target group
            Protocol='HTTP',  # The protocol to use (HTTP)
            Port=80,  # Port number to listen on
            VpcId=vpc_id,  # VPC ID where the target group resides
            HealthCheckProtocol='HTTP',  # Protocol for health checks
            HealthCheckPort='80',  # Port for health check (HTTP)
            HealthCheckPath='/polls/',  # Health check path (/polls/)
            HealthCheckIntervalSeconds=30,  # Health check interval set to 30 seconds
            HealthCheckTimeoutSeconds=5,  # Timeout for health check requests
            HealthyThresholdCount=2,  # Threshold for marking instance as healthy
            UnhealthyThresholdCount=2,  # Threshold for marking instance as unhealthy
            TargetType='instance'  # Target type is EC2 instances
        )
        # Get the ARN of the created target group
        target_group_arn = response['TargetGroups'][0]['TargetGroupArn']
        print(f"Target group created with ARN: {target_group_arn}")  # Print the ARN of the target group
        return target_group_arn  # Return the target group ARN
    except ClientError as e:
        print(f"Error creating target group: {e}")  # Print error message if creation fails
        return None  # Return None if creation fails

# Function to register EC2 instances with the target group
def register_targets(target_group_arn, instance_ids):
    try:
        # Prepare the list of targets (EC2 instances) to register
        targets = [{'Id': instance_id} for instance_id in instance_ids]
        # Register the targets with the specified target group
        elbv2.register_targets(
            TargetGroupArn=target_group_arn,  # Target group ARN
            Targets=targets  # List of instances to register
        )
        print(f"Registered instances {instance_ids} to the target group.")  # Print confirmation message
    except ClientError as e:
        print(f"Error registering targets: {e}")  # Print error message if registration fails

# Function to create a listener for the load balancer
def create_listener(lb_arn, target_group_arn):
    try:
        # Create an HTTP listener that forwards traffic to the target group
        elbv2.create_listener(
            LoadBalancerArn=lb_arn,  # Load Balancer ARN
            Protocol='HTTP',  # Protocol to listen for (HTTP)
            Port=80,  # Port to listen on (80)
            DefaultActions=[{
                'Type': 'forward',
                'TargetGroupArn': target_group_arn  # Forward traffic to the target group
            }]
        )
        print(f"Listener created for Load Balancer {lb_arn}")  # Print confirmation message
    except ClientError as e:
        print(f"Error creating listener: {e}")  # Print error message if creation fails

# Main function to handle the creation of load balancer, target group, and registration of instances
def main():
    instance_id = ['i-01b55b25eb0b60503']  # List of EC2 instance IDs to register in the target group
    sg_id = 'sg-045eebb087d4f0e9f'  # Security group ID for the load balancer

    # Describe VPCs and get the first available VPC ID
    vpcs = ec2.describe_vpcs()
    vpc_id = vpcs['Vpcs'][0]['VpcId']  # Extract the VPC ID
    
    # Get available subnets in the VPC
    subnets = get_subnets()
    # Select two subnets to use for the load balancer
    subnet_id = [subnets[0]['SubnetId'], subnets[1]['SubnetId']]
    
    # Create the Application Load Balancer (ALB)
    lb_arn = create_load_balancer(sg_id, subnet_id)

    # Create a target group within the VPC
    target_group_arn = create_target_group(vpc_id)

    # Register the EC2 instance with the target group
    register_targets(target_group_arn, instance_id)

    # Create a listener for the load balancer to forward traffic to the target group
    create_listener(lb_arn, target_group_arn)

# Entry point of the script
if __name__ == "__main__":
    main()  # Execute the main function
```
A detailed explanation is provided as comments in the code block above.

#### Results
After navigating to "EC2 > Target Groups" on AWS console, I confirmed that the Health check path is set to `/polls/`, and the Health check interval is set to `30 seconds`.
![alt text](image-59.png)


### [3] Access
I run the Django application again by using the command `python3 manage.py runserver 8000`. Then I opened the browser and and the polls page (http://54.152.128.37/polls/) of my EC2 instance.

#### Commands
- `python3`: This runs the Python 3 interpreter.
- `manage.py`: This is a Django utility script automatically generated when creating a Django project. It is used to perform various *administrative tasks* for the project, such as running the development server, creating migrations, or managing the database.
- `runserver`: This is the command that starts the Django development web server. By default, Django runs the server on port 8000, but we can specify a different port if needed.
- `8000`: This specifies the port number on which the server will listen.

#### Results
(After zoomed in)
![alt text](image-58.png)

## [Unmarked] Web interface for CloudStorage application

### [1] Create AWS DynamoDB table

#### 1.1 Create S3 bucket and upload target directory content

##### Python script `cloudstorage.py`
```python
import os
import boto3
import base64

ROOT_DIR = '.'
ROOT_S3_DIR = '22756463-cloudstorage'

s3 = boto3.client("s3")

bucket_region = 'us-east-1'

bucket_config = {'LocationConstraint': bucket_region} 


def upload_file(folder_name, file, file_name):
    print("Uploading %s" % file)

    try:
        s3.upload_file(file, ROOT_S3_DIR, folder_name+file_name)
    except Exception as error:
        print(error)
        pass

try:
    # Check if bucket exists
    s3.head_bucket(Bucket=ROOT_S3_DIR)
    print(f"Bucket {ROOT_S3_DIR} already exists.")
except Exception as error:
    # If bucket does not exist, create it
    print(f"Creating bucket {ROOT_S3_DIR}...")
    try:
        if bucket_region == 'us-east-1':
            # us-east-1 (N. Virginia) does not require LocationConstraint
            s3.create_bucket(Bucket=ROOT_S3_DIR)
        else:
            response = s3.create_bucket(
                Bucket=ROOT_S3_DIR,
                CreateBucketConfiguration=bucket_config
            )
            print(f"Bucket {ROOT_S3_DIR} created successfully.")
    except Exception as error:
        print(f"Error creating bucket: {str(error)}")
        raise


# parse directory and upload files
for dir_name, subdir_list, file_list in os.walk(ROOT_DIR, topdown=True):
    if dir_name != ROOT_DIR:
        for fname in file_list:
            # Check if the file is visible (not starting with a dot)
            if not fname.startswith('.'):
                upload_file("%s/" % dir_name[2:], "%s/%s" % (dir_name, fname), fname)

print("done")
```

##### Results
S3 bucket created with the target content:
![alt text](image-61.png)


#### 1.2 Run DynamoDB local
After I changed into the `dynamodb` directory in my Ubuntu environment, I run the DynamoDB local using the command `java -Djava.library.path=./DynamoDBLocal_lib -jar DynamoDBLocal.jar –sharedDb`.

##### Commands
- `java`: This is the Java command that starts the Java runtime environment. It’s necessary because DynamoDB Local is a Java-based program.

- `-Djava.library.path=./DynamoDBLocal_lib`: This argument specifies the path where the *necessary native libraries for DynamoDB Local* are located. In this case, ./DynamoDBLocal_lib refers to a directory in the current folder that contains the required libraries.

- `-jar DynamoDBLocal.jar`: This tells Java to execute the DynamoDBLocal.jar file, which is the executable file for DynamoDB Local.

- `–sharedDb`: This option tells DynamoDB Local to use a shared database file for all the tables, rather than creating separate databases for each access pattern or client. It simulates the single, global DynamoDB environment that you would have in AWS, allowing all clients and users to access the same tables and data.

##### Results



<div style="page-break-after: always;"></div>

# Lab 7

## Create an EC2 instance
I created an EC2 instance using the following 

### Python script `create_ec2_instance.py`
```python
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
```

### Results
Created an EC2 instance with ID `i-0baeaff2e48250061`.
![alt text](image-62.png)

## Install and configure Fabric
### [1] Install Fabric
I used the command `pip install fabric` to install Fabric in my Linux environment. Fabric is a Python library and command-line tool for streamlining the use of SSH for application deployment or systems administration tasks.

#### Commands
- `pip`: The Python’s package installer, which allows me to install and manage software packages written in Python.
- `install`: This is the specific command telling `pip` to install a package.
- `fabric`: This is the name of the package we want to install. Fabric is a high-level Python library that simplifies tasks such as deployment, automation, and managing remote servers via SSH.

#### Results
Successfully installed Fabric.
![alt text](image-63.png)

### [2] Create a config file in `~/.ssh`
I first changed into the directory by using command `cd ~/.ssh`. Then I created a config file by using the command `nano config`. 

#### Commands
- `cd`: This stands for "change directory." It is used to move into a different directory on the system.
- `~/.ssh`: The `~` symbol refers to the home directory (e.g., /home/username/ on Linux). The .ssh directory is a hidden folder in the home directory where SSH-related files, such as private/public keys and configuration files, are stored.
- `nano`: A text editor in Linux that opens files for editing in the terminal.
- `config`: The name of the file we want to edit or create. In this case, `config` is the SSH configuration file that contains your connection settings for SSH connections. If the file doesn't exist, nano will create it.

#### Content of `config`
```
Host 22756463-vm
	Hostname ec2-3-87-135-215.compute-1.amazonaws.com
	User ubuntu
	UserKnownHostsFile /dev/null
	StrictHostKeyChecking no
	PasswordAuthentication no
	IdentityFile ~/lab6/22756463-key.pem
```

#### Results
Created the file `config`:
![alt text](image-65.png)

### [3] Connect to the instance
I connected to the EC2 instance by activating the Python3 environment in my Linux environment. And then paste the following Python code line by line.

#### Python script and explanation
```python
from fabric import Connection  # Import the Connection class from the fabric library for managing SSH connections
c = Connection('22756463-vm')  # Establish an SSH connection to the machine named '22756463-vm'
result = c.run('uname -s')  # Run the 'uname -s' command on the remote machine to get the operating system name
```
A detailed explanation is provided as comments above.

#### Results
Connected to the EC2 instance.
![alt text](image-64.png)

## Use Fabric for automation

### Python script

### Results





<div style="page-break-after: always;"></div>

# Lab 8

<div style="page-break-after: always;"></div>

# Lab 9

