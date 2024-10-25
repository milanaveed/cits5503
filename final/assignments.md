# Exam Preparation

Exam topic:

•Networking (Week 7)

•IAM (Week 5)

•Miscellaneous (Week5 + Week 7 + Lab 5)

•AI (Week 8 + Labs 8&9)

•**DevOps (Week 10 + Lab 7)**

•Miscellaneous (Week7 + Week 9 + Lab 6)

**EC2 instance**: (short for Elastic Compute Cloud instance) is a AWS service that provides scalable computing capacity in the cloud.

## IAM

**An organisation has 5 departments and has separated out each of the IAM users into separate groups using paths following the pattern companybucket/department1/*, companybucket /department2/*, companybucket/department3/* etc.

Their IAM account names follow the pattern user@department1.company.com, user@department2.company.com etc.

You are tasked with securing a bucket that contains a folder for each of 5 departments in an organisation. Only people within a department can write to their own folder. Everyone can read from all folders.

Discuss the principles that you would use to create a policy that would achieve this objective.

Write the policy as a JSON file that you would use.**

Principles to consider:

1. **Least Privilege** : Grant users only the permissions they need to perform their tasks. In this case, each department's users need read access to all folders and write access only to their department's folder.
2. **Resource-based policies** : Define policies that restrict access based on the IAM paths and folder names in the bucket.
3. **Granular Access Control** : Ensure that permissions are granular/specific enough to allow specific access based on the bucket's folder structure.
4. **Path-based Permissions** : Use path-based folder structures in the S3 bucket to restrict write permissions based on the user's department.
5. **Read-Only Access for All** : Grant read permissions to all departments across the entire bucket to support the requirement that everyone can read from all folders.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowReadFromAllFolders",
      "Effect": "Allow",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::companybucket/*"
    },
    {
      "Sid": "AllowWriteToDepartment1Folder",
      "Effect": "Allow",
      "Action": "s3:PutObject",
      "Resource": "arn:aws:s3:::companybucket/department1/*",
      "Condition": {
        "StringLike": {
          "aws:username": "*@department1.company.com"
        }
      }
    },
    {
      "Sid": "AllowWriteToDepartment2Folder",
      "Effect": "Allow",
      "Action": "s3:PutObject",
      "Resource": "arn:aws:s3:::companybucket/department2/*",
      "Condition": {
        "StringLike": {
          "aws:username": "*@department2.company.com"
        }
      }
    },
    {
      "Sid": "AllowWriteToDepartment3Folder",
      "Effect": "Allow",
      "Action": "s3:PutObject",
      "Resource": "arn:aws:s3:::companybucket/department3/*",
      "Condition": {
        "StringLike": {
          "aws:username": "*@department3.company.com"
        }
      }
    },
    {
      "Sid": "AllowWriteToDepartment4Folder",
      "Effect": "Allow",
      "Action": "s3:PutObject",
      "Resource": "arn:aws:s3:::companybucket/department4/*",
      "Condition": {
        "StringLike": {
          "aws:username": "*@department4.company.com"
        }
      }
    },
    {
      "Sid": "AllowWriteToDepartment5Folder",
      "Effect": "Allow",
      "Action": "s3:PutObject",
      "Resource": "arn:aws:s3:::companybucket/department5/*",
      "Condition": {
        "StringLike": {
          "aws:username": "*@department5.company.com"
        }
      }
    }
  ]
}

```

## Network

**When an EC2 instance is created in AWS, it is assigned to a region and a Virtual Private Cloud (VPC). Describe how network addresses are allocated to a VPC and sub-networked when an EC2 instance is created. How is the EC2 connected to other machines and to the Internet?**

`The number after the slash indicates how many ones are in the subnet mask`

`IP addr = network addr + host addr`

`The network address is used to find the subnet in which the computer or the device is located`

`The host address is used to find the computer or the device in the subnet`

how network addresses are allocated to a VPC:

an address space (IPv4 and IPv6) with size /16 is allocated to a VPC: 172.31.0.0/16 (65536 addresses)

how sub-networked when an EC2 instance is created:

a size /20 default subnet is networked in each availability zone (4096 addresses).

In this case:

- a primary private IP address in the network address range is assigned to the default network interface (eth0) of the EC2 instance.
- a private DNS hostname that resolves to the private subnet range is given to the EC2 instance.
- a public IP address will be allocated to the EC2 instance.

Default VPC defines:

- An address space (IPv4 and IPv6): 172.31.0.0/16 (65,536 addresses)
- Subnet in each availability zone: e.g. 172.31.0.0/20 and 172.31.16.0/20
- Internet Gateway
- Main Route Table
- Default Security Group
- Default Network Access Control List (NACL)
- Default DHCP settings

To connect to other machines and to the internet:

access the main route table to know the reachable addresses of other machines in the VPC.

- if address is in local VPC, it can connect directly or through the router if the machine is in a different subnet.
- if address is not in local VPC, it can connect through the internet gateway according to NACLs.

ssh client:

1. generating the private and public keys for applying SSH client.
2. using AWS CLI command to authorize the user and push the public key to the instance.
3. connect to the instance using the associated private key after authentication.

## **Load balancing**

**Discuss the reasons why you would use Application Load Balancing and how this would be set up to load balance a Python Django application. Specifically, describe the configuration of the Listener and Target Group running the Python Django application.**

The steps to set up load balancer to Django application:

1. create security group.
2. set up the Django application to instances.
3. create a load balancer by specifying name, IP address type, avilable zones.
4. create target group.
5. configuring the target group and the Listener: name, protocol (HTTP), port (80), action (forward to the created target group), and the path for health check.
6. register targets with the configured target group.
7. deploy the services and check the healthy status of each target.

## Week 8

[16] Discuss the reasons why you would use Application Load Balancing and how this would be set up to load balance a Python Django application. Specifically, describe the configuration of the Listener and Target Group running the Python Django application.

[17] Describe 2 ways in which security is implemented in AWS networks at the network level. What are the similarities and differences between these 2 security implementations?

## Week 9

[18] When an EC2 instance is created in AWS, it is assigned to a region and a Virtual Private Cloud (VPC). Describe how network addresses are allocated to a VPC and sub-networked when an EC2 instance is created. How is the EC2 connected to other machines and to the Internet?

[19] What is DevOps and describe how you would implement the automation of creation of machines, configuration of software and deployment of application programs using AWS.

## Week 10

[20] Describe the 3 different types of Machine Learning Models that AWS Machine Learning allows you to use and describe examples of the types of questions you could answer with each one.

[21] Describe the different ways in which a Microservice Architecture can be implemented on AWS and what the benefits of this approach might be. How could authentication and authorisation be handled in this approach?

## Week 11

[22] You have been asked to create a project plan for the new machine learning model your company has asked you to build. List the main tasks and sub-tasks you would need to complete to create the model on AWS. How would you measure the accuracy of the model you created?
