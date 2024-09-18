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

TODO

### [3] Access the EC2 instance
I accessed the EC2 instance by opening the URL `http://54.152.128.37/polls/` in a browser.

#### Results
(Zoomed in)
![alt text](image-54.png)

## Set up an ALB

### [1] Create an application load balancer

#### Python script
```python
import boto3
from botocore.exceptions import ClientError

# Create a Boto3 EC2 and ELBv2 client
ec2 = boto3.client('ec2')
elbv2 = boto3.client('elbv2')

def get_subnets():
    subnets_response = ec2.describe_subnets()
    subnets = subnets_response['Subnets']
    
    # Filter subnets to only include those that are in available state
    available_subnets = [subnet for subnet in subnets if subnet['State'] == 'available']
    
    if len(available_subnets) < 2:
        raise Exception('Less than 2 available subnets in this region.')
    
    return available_subnets

def create_load_balancer(sg_id, subnets):
    try:
        response = elbv2.create_load_balancer(
            Name='22756463-load-balancer1',
            Subnets=subnets,
            SecurityGroups=[sg_id],
            Scheme='internet-facing',
            Type='application',
            IpAddressType='ipv4'
        )
        lb_arn = response['LoadBalancers'][0]['LoadBalancerArn']
        print(f"Load Balancer created with ARN: {lb_arn}")
        return lb_arn
    except ClientError as e:
        print(f"Error creating load balancer: {e}")
        return None


def create_target_group(vpc_id):
    try:
        response = elbv2.create_target_group(
            Name='22756463-target-group1',
            Protocol='HTTP',
            Port=80,
            VpcId=vpc_id,
            HealthCheckProtocol='HTTP',
            HealthCheckPort='80',
            TargetType='instance'
        )
        target_group_arn = response['TargetGroups'][0]['TargetGroupArn']
        print(f"Target group created with ARN: {target_group_arn}")
        return target_group_arn
    except ClientError as e:
        print(f"Error creating target group: {e}")
        return None


def register_targets(target_group_arn, instance_ids):
    try:
        targets = [{'Id': instance_id} for instance_id in instance_ids]
        elbv2.register_targets(
            TargetGroupArn=target_group_arn,
            Targets=targets
        )
        print(f"Registered instances {instance_ids} to the target group.")
    except ClientError as e:
        print(f"Error registering targets: {e}")


def create_listener(lb_arn, target_group_arn):
    try:
        elbv2.create_listener(
            LoadBalancerArn=lb_arn,
            Protocol='HTTP',
            Port=80,
            DefaultActions=[{
                'Type': 'forward',
                'TargetGroupArn': target_group_arn
            }]
        )
        print(f"Listener created for Load Balancer {lb_arn}")
    except ClientError as e:
        print(f"Error creating listener: {e}")


def main():
    sg_name = "22756463-sg"
    sg_description = "security group for development environment"
    student_number = '22756463'
    ami_id = 'ami-0a0e5d9c7acc336f1'
    key_name = "22756463-key"

    instance_id = ['i-01b55b25eb0b60503']
    sg_id = 'sg-045eebb087d4f0e9f'


    vpcs = ec2.describe_vpcs()
    vpc_id = vpcs['Vpcs'][0]['VpcId']
    

    subnets = get_subnets()
    subnet_id = [subnets[0]['SubnetId'], subnets[1]['SubnetId']]
    lb_arn = create_load_balancer(sg_id, subnet_id)

    target_group_arn = create_target_group(vpc_id)

    register_targets(target_group_arn, instance_id)


    create_listener(lb_arn, target_group_arn)

if __name__ == "__main__":
    main()
```



### [2] Health check


#### Python script 
```python
import boto3
from botocore.exceptions import ClientError

# Create a Boto3 EC2 and ELBv2 client
ec2 = boto3.client('ec2')
elbv2 = boto3.client('elbv2')

def get_subnets():
    subnets_response = ec2.describe_subnets()
    subnets = subnets_response['Subnets']
    
    # Filter subnets to only include those that are in available state
    available_subnets = [subnet for subnet in subnets if subnet['State'] == 'available']
    
    if len(available_subnets) < 2:
        raise Exception('Less than 2 available subnets in this region.')
    
    return available_subnets

def create_load_balancer(sg_id, subnets):
    try:
        response = elbv2.create_load_balancer(
            Name='22756463-load-balancer3',
            Subnets=subnets,
            SecurityGroups=[sg_id],
            Scheme='internet-facing',
            Type='application',
            IpAddressType='ipv4'
        )
        lb_arn = response['LoadBalancers'][0]['LoadBalancerArn']
        print(f"Load Balancer created with ARN: {lb_arn}")
        return lb_arn
    except ClientError as e:
        print(f"Error creating load balancer: {e}")
        return None


def create_target_group(vpc_id):
    try:
        response = elbv2.create_target_group(
            Name='22756463-target-group3',
            Protocol='HTTP',
            Port=80,
            VpcId=vpc_id,
            HealthCheckProtocol='HTTP',
            HealthCheckPort='80',
            HealthCheckPath='/polls/',  # Specify the /polls/ path for health checks
            HealthCheckIntervalSeconds=30,  # Health check interval set to 30 seconds
            HealthCheckTimeoutSeconds=5,  # Timeout for each health check (optional)
            HealthyThresholdCount=2,  # Number of consecutive successes to be considered healthy
            UnhealthyThresholdCount=2,  # Number of consecutive failures to be considered unhealthy
            TargetType='instance'
        )
        target_group_arn = response['TargetGroups'][0]['TargetGroupArn']
        print(f"Target group created with ARN: {target_group_arn}")
        return target_group_arn
    except ClientError as e:
        print(f"Error creating target group: {e}")
        return None


def register_targets(target_group_arn, instance_ids):
    try:
        targets = [{'Id': instance_id} for instance_id in instance_ids]
        elbv2.register_targets(
            TargetGroupArn=target_group_arn,
            Targets=targets
        )
        print(f"Registered instances {instance_ids} to the target group.")
    except ClientError as e:
        print(f"Error registering targets: {e}")


def create_listener(lb_arn, target_group_arn):
    try:
        elbv2.create_listener(
            LoadBalancerArn=lb_arn,
            Protocol='HTTP',
            Port=80,
            DefaultActions=[{
                'Type': 'forward',
                'TargetGroupArn': target_group_arn
            }]
        )
        print(f"Listener created for Load Balancer {lb_arn}")
    except ClientError as e:
        print(f"Error creating listener: {e}")


def main():
    instance_id = ['i-01b55b25eb0b60503']
    sg_id = 'sg-045eebb087d4f0e9f'


    vpcs = ec2.describe_vpcs()
    vpc_id = vpcs['Vpcs'][0]['VpcId']
    

    subnets = get_subnets()
    subnet_id = [subnets[0]['SubnetId'], subnets[1]['SubnetId']]
    lb_arn = create_load_balancer(sg_id, subnet_id)

    target_group_arn = create_target_group(vpc_id)

    register_targets(target_group_arn, instance_id)


    create_listener(lb_arn, target_group_arn)

if __name__ == "__main__":
    main()
```


#### Results
After navigating to "EC2 > Target Groups" on AWS console, I confirmed that the Health check path is set to `/polls/`, and the Health check interval is set to `30 seconds`.
![alt text](image-59.png)


### [3] Access
I run the Django application again by using the command `python3 manage.py runserver 8000`.



#### Results
(After zoomed in)
![alt text](image-58.png)


<div style="page-break-after: always;"></div>

# Lab 7

<div style="page-break-after: always;"></div>

# Lab 8

<div style="page-break-after: always;"></div>

# Lab 9

