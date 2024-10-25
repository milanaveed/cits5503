# Exam Preparation

Exam topic:

~~•Networking (Week 7)~~

~~•IAM (Week 5)~~

~~•Miscellaneous (Week5 + Week 7 + Lab 5)~~

~~•AI (Week 8 + Labs 8&9)~~

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

How network addresses are allocated to a VPC:

* Assign the VPC a CIDR block , such as `10.0.0.0/16 (65,536 IP addresses)`, which defines the *IP address range* for all resources within the VPC.
* This CIDR block is then divided into subnets.

How sub-networked when an EC2 instance is created:

* **Subnets** are created within a VPC, each assigned a specific portion of the VPC's IP range. For example, a VPC with a CIDR block of `10.0.0.0/16` could have subnets like:

  * `10.0.1.0/24` for one subnet (providing 256 addresses),
  * `10.0.2.0/24` for another subnet, and so forth.
* Subnets can be designated as **public** or  **private** :

  * **Public Subnets** : Have Internet access via an  **Internet Gateway (IGW)** .
  * **Private Subnets** : No direct Internet access; use **NAT Gateway** for outbound connectivity if needed.
* (IP allocation) When an EC2 instance is launched within a subnet, it is assigned:

  * **Private IP** : Each EC2 instance gets a private IP within its subnet.
  * **Public IP** : Optionally assigned in a public subnet for Internet access; static **Elastic IP** can be used for consistent access.

To connect to other machines:

* **Route Tables** : Each subnet is associated with a route table that defines the traffic flow rules. Route tables have entries specifying how packets are routed within the VPC, between subnets, and externally.
* **Security Groups and Network ACLs** : Both **Security Groups** (instance-level firewall) and **Network Access Control Lists (NACLs)** (subnet-level firewall) define access rules for inbound and outbound traffic.

Access the main **route table** to know the reachable addresses of other machines in the VPC.

- if address is in local VPC, it can connect directly or through the router if the machine is in a different subnet.
- if address is not in local VPC, it can connect through the internet gateway according to NACLs.

To connect to other networks:

* **Internet Gateway (IGW)** : Provides public Internet access for instances in public subnets.
* **NAT Gateway** : Enables private instances to access the Internet without direct exposure.


**Describe 2 ways in which security is implemented in AWS networks at the network level. What are the similarities and differences between these 2 security implementations?**

**Similarities**:

* Both control **inbound and outbound traffic** and use IP addresses and port rules.
* Both are components of AWS **VPC security** and provide an additional layer of network protection.

**security group**: it controls the traffic that is allowed to reach and leave the resources at the instance level.

1. support rules only.
2. stateful: If an inbound request is allowed, the response is automatically allowed.
3. instance-level

Use Case : Commonly used for controlling access to individual instances, such as allowing SSH or HTTP access.

**Network ACLs (network access control lists)**: it allows or denies specific traffic to reach and leave the resources at subnet level.

1. support and deny rules.
2. stateless: Each inbound and outbound rule must be explicitly defined; no automatic responses are allowed.
3. subnet level

Use Case : Used for broader control of subnet traffic, such as blocking specific IP ranges from accessing an entire subnet.

## **ALB (load balancing) (needs improve))**

**Discuss the reasons why you would use Application Load Balancing and how this would be set up to load balance a Python Django application. Specifically, describe the configuration of the Listener and Target Group running the Python Django application.**

Steps to set up load balancer to Django application:

1. set up the Django application to instances.
2. create and configure security group.
3. create a load balancer by specifying name, IP address type, avilable zones.
4. create target group.
5. configuring the target group and the listener: name, protocol (HTTP), port (80), action (forward to the created target group), and the path for health check.
6. register targets with the configured target group.

## ML/AI

- Underfitting: model is too “simple” to represent all the relevant class characteristics
  - High bias and low variance
  - High training error and high test error
- Overfitting: model is too “complex” and fits irrelevant characteristics (noise) in the data
  - Low bias and high variance
  - Low training error and high test error

**Describe the 3 different types of Machine Learning Models that AWS Machine Learning allows you to use and describe examples of the types of questions you could answer with each one.**

https://docs.aws.amazon.com/machine-learning/latest/dg/types-of-ml-models.html

**Binary Classification Model**

"Is this email spam or not spam?"

"Will the customer buy this product?"

"Is this product a book or a farm animal?"

"Is this review written by a customer or a robot?"

**Multiclass Classification Model**

"Is this product a book, movie, or clothing?"

"Is this movie a romantic comedy, documentary, or thriller?"

"Which category of products is most interesting to this customer?"

**Regression Model**

"What will the temperature be in Seattle tomorrow?"

"For this product, how many units will sell?"

"What price will this house sell for?"

**You have been asked to create a project plan for the new machine learning model your company has asked you to build. List the main tasks and sub-tasks you would need to complete to create the model on AWS. How would you measure the accuracy of the model you created?**

- install libraries for running jupyter notebooks and training
- prepare a sagemaker session:

  - get the SageMaker execution role ARN
  - create a S3 bucket for holding input and output
- prepare dataset:

  - collect labelled data and setup a target variable and a list of feature variables
  - preprocess data (data cleaning, data transform, feature scaling: create categorical variables, convert categorical variables to dummy variables, drop columns, convert boolean columns to numeric)
  - split into training, validation and test dataset
  - upload train and validation datasets to S3 bucket
- select a machine learning model
- set up tuning job name and configuration (hyperparameters ranges, tuning strategy, total number of training jobs, max number of parallel jobs, metrics used for tuning)
- specify the machine learning algorithm used for tuning job (retrieve training image, specify S3 paths for datasets, define input data for training and validation channels, specify output location, define compute resou1rces, specify IAM role, static hyperparameters for the algorithm, stopping condition)
- launch the tuning job: train the model using training set and tuning hyperparameters using validation set
- evaluated the model using test dataset, use metrics like AUC score, f1, precision, recall

Using evaluation metrics to assess the accuracy of each model:

- Binary classification – Accuracy, Precision, AUC
- Multiclass classification – Precision, Recall, F1, AUC
- Regression – RMSE, Accuracy

## Architecture

**Describe the different ways in which a Microservice Architecture can be implemented on AWS and what the benefits of this approach might be. How could authentication and authorisation be handled in this approach?**



## DevOps

**What is DevOps and describe how you would implement the automation of creation of machines, configuration of software and deployment of application programs using AWS.**

What is DevOps:

1. Creating automation for the entire build/test/release cycle,
2. allows Development, Test and Production environments to be built, tested and deployed easily and systematically,
3. Allows new components to be added automatically,
4. Could be done manually with the help of scripts but there are software environments that manage remote communication and execution of resource creation, software installation and configuration.

How to implement:

1. Using fabric to connect to an SSH server and executing commands remotely.
2. Using the version control tool AWS CodeCommit to maintain changes in the source code.
3. Using AWS CodePipeline to perform Continuous Integration/Continuous Delivery (CI & CD) service for updating code.
4. Using AWS CodeBuild to compile source code, run tests, and produce software packages.
5. Using AWS CodeDeploy to test and deploy new code.
6. Using AWS Chef to manage machines. stacks, layers and applications can be established.

- A layer with a recipe specifies one category of software. Edit our own chef recipe. In the instance interface, we can manage EC2 instances for the particular layer. EC2 will install and configure software according to chef recipe after it starts.
