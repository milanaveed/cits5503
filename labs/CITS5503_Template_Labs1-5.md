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

#### Explanation of commands:
- `sudo`: allows us to run the command with elevated (root) privileges.
- `apt`: the command-line tool used to interact with the Advanced Package Tool (APT), the package management system used by Debian-based distributions. APT manages the installation, upgrade, and removal of software packages.
- `-y`: automatically answers "yes" to any prompts that might come up during the upgrade process.

### [2] Install awscli
`awscli` stands for Amazon Web Services Command Line Interface. It's a unified tool that provides a consistent interface for interacting with all of Amazon Web Services (AWS). I installed and updated awscli through commands `sudo apt install awscli` and `pip3 install awscli --upgrade`.

### [3] Configure AWS

[Refer to the marking rubrics for sufficient step-by-step description.]

### [4] Install boto3

[Refer to the marking rubrics for sufficient step-by-step description.]

## Test the installed environment

### [1] Test the AWS environment

[Refer to the marking rubrics for sufficient step-by-step description.]

### [2] Test the Python environment

[Refer to the marking rubrics for sufficient step-by-step description.]

### [3] Write a Python script

[Refer to the marking rubrics for sufficient step-by-step description.]

<div style="page-break-after: always;"></div>

# Lab 2

<div style="page-break-after: always;"></div>

# Lab 3

<div style="page-break-after: always;"></div>

# Lab 4

<div style="page-break-after: always;"></div>

# Lab 5

