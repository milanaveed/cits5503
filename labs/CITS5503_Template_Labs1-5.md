<div style="display: flex; flex-direction: column; justify-content: center; align-items: center; height: 100vh;">

  <h2>Labs 1-5</h2>
  
  <p>Student ID: 22756463</p>
  <p>Student Name: Mila (Yue) Zhang</p>

</div>

# Lab 1

## AWS Account and Log in

### [1] Log into an IAM user account
After opening the [login page](https://489389878001.signin.aws.amazon.com/console), I entered my IAM user name "22756463@student.uwa.edu.au" and the initial password provided by the Unit Coordinator. Then I changed my password after login.

![login](Screenshot%202024-08-15%20141248.png)

![console](image.png)

### [2] Search and open Identity Access Management
After clicking my user account and selecting the Security Credentials tab, I created an access key and noted the Access Key ID and the secret access key down.

![alt text](image-1.png)

## Set up recent Linux OSes
### [1] Download Ubuntu OS 22.04.3
I downloaded Ubuntu OS 22.04.3 from the Microsoft Store as recommended by a lab facilitator.

![alt text](image-2.png)

### [2] Update WSL
Since there was an old version of WSL installed on my laptop, I used command `wsl --update` to update the WSL.
![alt text](image-3.png)

## Install Linux packages

### [1] Install Python 3.8.x and above
Since the recent Ubuntu versions such as 22.04.3 LTS have Python 3.8.x installed, I updated the packages to obtain the latest version through commands `sudo apt update` and `sudo apt -y upgrade`. After checking the latest version through command `python3 -V`, now we can see I have version `Python 3.10.12` installed. Then I installed pip3 through command `sudo apt install -y python3-pip` for future Python library management.

#### Commands:
- `sudo`: allows us to run the command with elevated (root) privileges.
- `apt`: the command-line tool used to interact with the Advanced Package Tool (APT), the package management system used by Debian-based distributions. APT manages the installation, upgrade, and removal of software packages.
- `-y`: automatically answers "yes" to any prompts that might come up during the upgrade process.

### [2] Install awscli
`awscli` stands for Amazon Web Services Command Line Interface. It's a unified tool that provides a consistent interface for interacting with all of Amazon Web Services (AWS). I installed and updated awscli through commands `sudo apt install awscli` and `pip3 install awscli --upgrade`.

#### Commands:
- `sudo`: allows us to run the command with elevated (root) privileges.
- `apt`: the command-line tool used to interact with the Advanced Package Tool (APT), the package management system used by Debian-based distributions. APT manages the installation, upgrade, and removal of software packages.
- `pip3`: package installer for Python 3 which allows us to install and manage Python packages.

#### Results:
```bash
mila@DESKTOP-N95AEOP:~$ sudo apt install awscli
[sudo] password for mila:
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
awscli is already the newest version (1.22.34-1).
0 upgraded, 0 newly installed, 0 to remove and 2 not upgraded.
------------------------------------------------------------------------------
mila@DESKTOP-N95AEOP:~$ pip3 install awscli --upgrade
Successfully installed awscli-1.34.2 botocore-1.35.2
```

### [3] Configure AWS
I set up and managed my AWS credentials and configuration settings for the AWS Command Line Interface by using command `aws configure`. I entered information of my AWS Access Key ID, AWS Secret Access Key, default region name according to my student number in the table (my student number 22756463 was allocated to region with name "us-east-1"), and the default output format.


### [4] Install boto3
I installed the "boto3" library which is the official AWS SDK (software development kit) for Python through command `pip3 install boto3`. "boto3" allows Python developers to write software that use Amazon services like S3, EC2 and so on. After installation, we can import the library in Python scripts and interact with AWS services.


## Test the installed environment

### [1] Test the AWS environment
I tested the AWS environment by retrieving a list of all available AWS regions for EC2 and display the information in a table format.

#### Commands
- `aws`: the AWS Command Line Interface. It is the tool we use to interact with AWS services directly from the command line or terminal.
- `ec2`: EC2 stands for the AWS Elastic Compute Cloud. By specifying `ec2` in this command, we tell the AWS CLI we want to perform an action associated with the EC2 service.
- `describe-regions`: the action we want to perform within the EC2 service. It lists all available AWS regions (geographical areas that have various data centres) for the EC2 service.
- `--output`: controls the format of the command's output. Some typical formats are "json", "table", "text", "yaml" and so on.
- `--output table`: this part specifies that the output should be formatted as a table.

#### Results
![result](image-7.png)
### [2] Test the Python environment
I tested the Python3 environment by activating the Python3 interactive shell and entered some Python code.

#### Commands
```python
python3
>>> import boto3
>>> ec2 = boto3.client('ec2')
>>> response = ec2.describe_regions()
>>> print(response)
```
- `import boto3`: imports the "boto3" library which is the AWS Software Development Kit for Python. After importing the package, our Python scripts can interact with AWS services.
- `ec2 = boto3.client('ec2)`: creates a client object for the EC2 service so we can make specific requests to the EC2 service.
- `response = ec2.describe_regions()`: calls the "describe_regions()" method of the EC2 client object and saves the returned information into a variable called "response".
- `print(response)`: prints out the variable "response" which is a dictionary containing information about the regions.

#### Results
```
{'Regions': [{'Endpoint': 'ec2.ap-south-1.amazonaws.com', 'RegionName': 'ap-south-1', 'OptInStatus': 'opt-in-not-required'}, {'Endpoint': 'ec2.eu-north-1.amazonaws.com', 'RegionName': 'eu-north-1', 'OptInStatus': 'opt-in-not-required'}, {'Endpoint': 'ec2.eu-west-3.amazonaws.com', 'RegionName': 'eu-west-3', 'OptInStatus': 'opt-in-not-required'}, {'Endpoint': 'ec2.eu-west-2.amazonaws.com', 'RegionName': 'eu-west-2', 'OptInStatus': 'opt-in-not-required'}, {'Endpoint': 'ec2.eu-west-1.amazonaws.com', 'RegionName': 'eu-west-1', 'OptInStatus': 'opt-in-not-required'}, {'Endpoint': 'ec2.ap-northeast-3.amazonaws.com', 'RegionName': 'ap-northeast-3', 'OptInStatus': 'opt-in-not-required'}, {'Endpoint': 'ec2.ap-northeast-2.amazonaws.com', 'RegionName': 'ap-northeast-2', 'OptInStatus': 'opt-in-not-required'}, {'Endpoint': 'ec2.ap-northeast-1.amazonaws.com', 'RegionName': 'ap-northeast-1', 'OptInStatus': 'opt-in-not-required'}, {'Endpoint': 'ec2.ca-central-1.amazonaws.com', 'RegionName': 'ca-central-1', 'OptInStatus': 'opt-in-not-required'}, {'Endpoint': 'ec2.sa-east-1.amazonaws.com', 'RegionName': 'sa-east-1', 'OptInStatus': 'opt-in-not-required'}, {'Endpoint': 'ec2.ap-southeast-1.amazonaws.com', 'RegionName': 'ap-southeast-1', 'OptInStatus': 'opt-in-not-required'}, {'Endpoint': 'ec2.ap-southeast-2.amazonaws.com', 'RegionName': 'ap-southeast-2', 'OptInStatus': 'opt-in-not-required'}, {'Endpoint': 'ec2.eu-central-1.amazonaws.com', 'RegionName': 'eu-central-1', 'OptInStatus': 'opt-in-not-required'}, {'Endpoint': 'ec2.us-east-1.amazonaws.com', 'RegionName': 'us-east-1', 'OptInStatus': 'opt-in-not-required'}, {'Endpoint': 'ec2.us-east-2.amazonaws.com', 'RegionName': 'us-east-2', 'OptInStatus': 'opt-in-not-required'}, {'Endpoint': 'ec2.us-west-1.amazonaws.com', 'RegionName': 'us-west-1', 'OptInStatus': 'opt-in-not-required'}, {'Endpoint': 'ec2.us-west-2.amazonaws.com', 'RegionName': 'us-west-2', 'OptInStatus': 'opt-in-not-required'}], 'ResponseMetadata': {'RequestId': '4a4ee39e-9960-4855-855f-1d1d31c7d4ed', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': '4a4ee39e-9960-4855-855f-1d1d31c7d4ed', 'cache-control': 'no-cache, no-store', 'strict-transport-security': 'max-age=31536000; includeSubDomains', 'vary': 'accept-encoding', 'content-type': 'text/xml;charset=UTF-8', 'content-length': '2890', 'date': 'Wed, 21 Aug 2024 12:57:45 GMT', 'server': 'AmazonEC2'}, 'RetryAttempts': 0}}
```

### [3] Write a Python script
To tabulate the above returned response, I used the Python code below.

#### Commands
- `pip3 install tabulate`: Since the package "tabulate" was not installed before, I install the library first, so we can easily format tabular data by using functions of this library.

```python
import boto3
from tabulate import tabulate

# Create an EC2 client object
ec2 = boto3.client('ec2')

# Call the describe_regions method and store in the variable response
response = ec2.describe_regions()

# This list comprehension iterates over each dictionary in "response['Regions']". Then it extracts the Endpoint and RegionName from each dictionary and stores them as a list of tuples
content = [(region['Endpoint'], region['RegionName']) for region in response['Regions']]

# Define the column names for the table
col_names = ["Endpoint", "RegionName"]

# Print the table using tabulate
print(tabulate(content, col_names, tablefmt="pretty"))
```

#### Results
![alt text](image-8.png)


<div style="page-break-after: always;"></div>

# Lab 2

## Create an EC2 instance using awscli

### [1] Create a security group
I created a new security group in Amazon EC2 through the command `aws ec2 create-security-group --group-name 22756463-sg --description "security group for development environment"`. This security group will act as virtual firewalls to control inbound and outbound traffic (traffic coming into the instances and traffic going out from the instances) to the EC2 instances.

#### Commands
- `aws ec2`: refers to the AWS EC2 service. By specifying this, we are using the AWS EC2 service through the command line.
- `create-security-group`: the action we are doing given this command line. It creates a new security group in the default VPC (Virtual Private Cloud) given VPC is not specified in this case.
- `--group-name`: this flag is used to specify the name of the security group. 
- `-sg`: "sg" stands for security group. This suffix is a common convention to specify that this is a security group.
- `--description`: this flag is used to set the description for the security group, so we can identify the purpose of this security group later.
  
#### Results
Created a security group named "22756463-sg".
```
{
    "GroupId": "sg-0ae5c80f51af3b210"
}
```

### [2] Authorise inbound traffic for ssh
I authorised inbound traffic by using command `aws ec2 authorize-security-group-ingress --group-name 22756463-sg --protocol tcp --port 22 --cidr 0.0.0.0/0`. This command allowed inbound SSH (port 22) traffic to reach my EC2 instance from any IP address (by specifying "0.0.0.0/0"), as long as the instance is associated with the security group "22756463-sg". This rule is applied using the TCP protocol.

#### Commands
- `aws ec2 authorize-security-group-ingress`: This is used to add a rule to an existing security group to allow inbound traffic to the security group.
- `--group-name 22756463-sg`: Specifies the name of the security group we are modifying.
- `--protocol tcp`: Defines the protocol that is allowed. In this case, tcp is the Transmission Control Protocol, which is the protocol used for reliable communication over the internet (commonly used for SSH, HTTP, HTTPS, etc.).
- `--port 22`: `--port` Specifies the port number to allow inbound traffic on.
In this case, port 22 is used for SSH (Secure Shell), which is commonly used for remote access to Linux servers.
- `--cidr 0.0.0.0/0`: The CIDR (Classless Inter-Domain Routing) block represents the range of IP addresses that are allowed to connect. "0.0.0.0/0" represents all IP addresses, meaning this rule will allow SSH traffic from anywhere in the world. (This is generally not secure and should be restricted to a specific IP range or address whenever possible.)
- SSH (Secure Shell): A *network protocol* used to securely *access and manage remote servers* over an unsecured network. It allows us to establish a secure, encrypted connection between our local machine and a remote server, enabling us to execute commands, transfer files, and perform administrative tasks on that server.

#### Results
```
{
    "Return": true,
    "SecurityGroupRules": [
        {
            "SecurityGroupRuleId": "sgr-093d071b1a0fd2236",
            "GroupId": "sg-0ae5c80f51af3b210",
            "GroupOwnerId": "489389878001",
            "IsEgress": false,
            "IpProtocol": "tcp",
            "FromPort": 22,
            "ToPort": 22,
            "CidrIpv4": "0.0.0.0/0"
        }
    ]
}
```

### [3] Create a key pair
I generated a new key pair, extracted the private key and saved it to a file in the file format ".pem" which is mainly used for SSH access to EC2 instances. This private key file will be required when I SSH into my EC2 instance.

#### Commands
- `aws ec2 create-key-pair`: Used to create an SSH key pair for securely connecting to an Amazon EC2 instance. A key pair consists of a public key (stored by AWS) and a private key (saved by me), which are used to securely connect to an EC2 instance via SSH.
- `--key-name`: Specifies the name of the key pair. The key name must be unique within my AWS account for that region.
- `--query 'KeyMaterial'`: The `--query` option filters the output of the command. 'KeyMaterial' is the part of the *returned data* that contains the actual *private key* in plain text format, which I need to connect to EC2 instances via SSH. This ensures that only the private key (KeyMaterial) is retrieved from the full response that AWS returns.
- `--output text`: This option specifies that the output should be in plain text format, rather than JSON or any other format. This ensures that the private key is displayed in a simple, readable text format, which can then be saved to a file.
- `> 22756463-key.pem`: The `>` operator redirects the output of the command to a file named `22756463-key.pem`. This file will contain the private key (in .pem format), which I will later use to connect to my EC2 instance via SSH.
- ".pem" file: A ".pem" file (Privacy Enhanced Mail) is a file format that typically contains a private key and/or a public key. It is used in various security and encryption contexts, most commonly for establishing secure communication over the internet (such as SSH and HTTPS). In AWS, .pem files are primarily used for SSH access to EC2 instances.
- `chmod 400 22756463-key.pem`: This command sets the file permissions such that only the file owner can read the 22756463-key.pem file, and no one else (group or others) can read, write, or execute the file. `chmod` is the change mode command in Unix/Linux systems. It is used to change the permissions of a file or directory. Permissions control who can read, write, or execute a file. `400` is the permission code that specifies what permissions are being applied to the file. The first digit represents the owner permission, the second digit represents the group permission, and the last digit represent the permission of others. "4" represents read permission while "0" means no permission. `22756463-key.pem` specifies the name of the file for which the permissions are being changed.

#### Results
Generated a new key pair, extracted the private key and saved it into "22756463-key.pem". Then changed the file permission to be read only by the owner.

### [4] Create the instance
I created an instance located in the region "US East (N. Virginia)" according to my student number and the allocation table. I used the command ``aws ec2 run-instances --image-id ami-0a0e5d9c7acc336f1 --security-group-ids 22756463-sg --count 1 --instance-type t2.micro --key-name 22756463-key --query 'Instances[0].InstanceId'.

#### Commands
- `aws ec2 run-instances`: This command is used to launch (run) one or more EC2 instances in the AWS cloud.
- `--image-id`: Specifies the Amazon Machine Image (AMI) that will be used to launch the instance.
- `--security-group-ids`: This specifies the security group(s) that will be associated with the instance. The security group acts as a *virtual firewall* that controls inbound and outbound traffic.
- `--count`: Specifies the number of EC2 instances to launch.
- `--instance-type`: Specifies the type of EC2 instance to launch. `t2.micro` is a small, general-purpose instance type with 1 vCPU and 1 GB of RAM. It is suitable for low-traffic applications or testing and is often eligible for the AWS Free Tier.
- `--key-name`: Specifies the name of the SSH key pair that will be used to access the instance.
- `--query 'Instances[0].InstanceId'`: `--query` is used to filter the output of the command. This queries the result to return only the Instance ID of the first launched instance.

#### Results
The Instance ID of the newly launched instance was returned:
```
"i-04c3576556495a2d1"
```

### [5] Add a tag to your Instance
I added a tag to my EC2 instance created in step 4 by using the command `aws ec2 create-tags --resources i-04c3576556495a2d1 --tags Key=Name,Value=22756463`. The tag is useful for identifying and organising the instance.

#### Commands
- `aws ec2 create-tags`: This command is used to assign metadata, called tags, to an AWS resource such as an EC2 instance, volume, or other AWS resources. Tags are *key-value pairs* that allow me to organise, identify, and manage my resources more easily.
- `--resources`: Specifies which AWS resources (like EC2 instances, volumes, etc.) I want to tag.
- `--tags Key=Name,Value=22756463`: `--tags` defines the tag(s) I want to apply to the resource. `Key=Name` specifies the key for the tag. In AWS, "Name" is commonly used as a tag key to give the resource a human-readable name. `Value=22756463` specifies the value for the "Name" tag.

#### Results
Applied a tag to my EC2 instance with the ID "i-04c3576556495a2d1". The tag has a key of "Name" and a value of "22756463".

### [6] Get the public IP address
I retrieved the public IP address of the EC2 instance I created in step 4 by using command `aws ec2 describe-instances --instance-ids i-04c3576556495a2d1 --query 'Reservations[0].Instances[0].PublicIpAddress'`.

#### Commands
- `aws ec2 describe-instances`: The command is used to retrieve details about specific EC2 instances.
- `--instance-ids`: This flag specifies the ID(s) of the EC2 instances I want to describe.
- `--query 'Reservations[0].Instances[0].PublicIpAddress'`: `--query` filters the output to retrieve only the information I need. This query navigates the JSON structure returned by the `describe-instances` command to extract the public IP address of the first instance in the first reservation.

#### Results
Public IP address of the specified EC2 instance was returned:
```
"54.175.111.6"
```

### [7] Connect to the instance via ssh
I connected to an Ubuntu EC2 instance located at public address "54.175.111.6" using SSH by the command `ssh -i 22756463-key.pem ubuntu@54.175.111.6`.

#### Commands
- `ssh`: This is the command for Secure Shell (SSH), a protocol used to securely connect to remote servers. SSH enables encrypted communication between the client (my machine) and the server (in this case, an EC2 instance).
- `-i 22756463-key.pem`: `-i` specifies the identity file. In this case is the private key that I use to authenticate with the remote server.
- `ubuntu`: This is the AMI (Amazon Machine Image) *username* that I am using to log into the remote server.
- `@54.175.111.6`: `@` separates the username (ubuntu) from the server's IP address or hostname. `54.175.111.6` is the public IP address of the EC2 instance I am connecting to.

#### Results
```
Welcome to Ubuntu 22.04.4 LTS (GNU/Linux 6.5.0-1022-aws x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro

 System information as of Fri Sep  6 13:40:19 UTC 2024

  System load:  0.08              Processes:             97
  Usage of /:   20.7% of 7.57GB   Users logged in:       0
  Memory usage: 21%               IPv4 address for eth0: 172.31.95.57
  Swap usage:   0%
```

### [8] List the created instance using the AWS console


## Create an EC2 instance with Python Boto3

## Use Docker inside a Linux OS

### [1] Install Docker

### [2] Start Docker

### [3] Enable Docker

### [4] Check the version

### [5] Build and run an httpd container

### [6] Other docker commands


<div style="page-break-after: always;"></div>

# Lab 3

<div style="page-break-after: always;"></div>

# Lab 4

<div style="page-break-after: always;"></div>

# Lab 5

