## **Cloud computing characteristics**

pros:

1. Reducing IT costs for hiring IT experts and maintaining local host machines.
2. No up-front investment, pay-as-you-go model
3. Scalability: quickly scale up/down as damand varies.
4. Security: a collection of security measures designed to protect cloud services.

cons:

1. downtime issues due to possible outages of cloud-based services.
2. privacy issues due to store important data on external service providers.
3. cybersecurity issues due to the exposure of vulnerabilities in system components.
4. cost issues for small scale and short-term projects.

Problems of running ones own data centers:

- difficult to scale up or down
- difficult to manage resources
- difficult to perform maintenance

XaaS cloud computing:
![image](services.png)

## **DevOps, Security, Networking**

**[18] [10 Points] Describe 2 ways in which security is implemented in AWS networks at the network level. What are the similarities and differences between these 2 security implementations?**

https://www.knowledgehut.com/tutorials/aws/nacl-vs-security-groups#:~:text=Security%20groups%20are%20associated%20with,firewall%20to%20protect%20EC2%20instances.

security group: it controls the traffic that is allowed to reach and leave the resources at the instance level.

1. support rules only.
2. stateful.
3. associate with an instance of a service.
4. all rules are applied to an instance.

Network ACLs: it allows or denies specific traffic to reach and leave the resources at subnet level.

1. support and deny rules.
2. stateless.
3. multiple subnets can be bound with a single NACL.
4. rules are applied in the order of their priority.

![image](sg-nacl.png)

## **Storage, Database in AWS**

**Describe EBS and what features it offers.**

Amazon EBS (Amazon Elastic Block Store) provides block level storage volumes for use with EC2 instances.

1. It can replicate data through multiple servers so the data won't be lost if a single server is down.
2. It can encrypt data automatically in EBS data volumes, boot volumes, and snapshots.
3. It can create a snapshot of the EBS volume which can be recreated at any time.
4. It can increase size automatically with little downtime.
5. It can provide lower latency, higher IOPS, and higher throughput service using SSD or HDD based on the demand.
6. It can be placed in specific availability zones.

## **Web architecture and framework**

**[22] [10 points] Describe the different ways in which a Microservice Architecture can be implemented on AWS and what the benefits of this approach might be. How could authentication and authorisation be handled in this approach?**

Microservices can be hosted on Lambda (Serverless), Containers, or can be other Django/Ruby/NodeJS apps.

Front end is via an API Gateway that defines a programmatic interface to the services

Benefits of Rest API based API Gateway are:

- Language agnostic
- Maintains an interface that encapsulates implementation
- Can use SQS to allow queues to invoke APIs
  Need to handle authentication and authorisation for the API
- Use IAM either directly or through API Gateway Resource Policies
- Use Cognito
- Use API keys
- Use an external service through Lambda

## **Docker and container**

A container is a standard unit of software that packages up the application and all its dependencies and libraries by virtualising the operating system.

Docker offers the ability to run multiple applications within the same host OS, sharing underlying resources.

Docker vs Container:

1. Similarity: Both containers and docker images allow users to specify application dependencies and configurations and to describe everything necessary for a machine to run the application.
2. Differences: All Containers use the same underlying OS but present various parts of the OS as if they were dedicated to the running system, whereas Docker is an application that provides a secure and isolated environment to run containers.

Docker vs VMBox:

1. Similarity: Both Docker and VirtualBox are virtualisation tools running on the computer.
2. Differences: VirtualBox is an virtualization app that create virtual machines that are isolated at the hardware level, whereas Docker is a containerization app that isolates apps at application level.

## **S3 bucket**

**Describe what S3 is and discuss its similarities and differences with the data store DynamoDB.**

Simple Storage Service (S3) is an AWS cloud service used for object storage. S3 buckets are provided to users to store file objects. Permission and authentication settings are available for users to determine who is allowed or not allowed to perform specific actions with the resources in the bucket.

Similarities:

1. they are both storage-based services,
2. high performance, scalability, availability, security.
   Differences:
3. S3 stores all objects with data and metadata in the bucket, whereas DynamoDB is a NoSQL database storing key-value pairs.
4. S3 mainly stores media files such as images, videos, sound files etc., while DynamoDB mainly stores document-based files.
5. S3 has the version control mechanism while DynamoDB doesn't.


**[22] [10 points] Describe the different ways in which a Microservice Architecture can be implemented on AWS and what the benefits of this approach might be. How could authentication and authorisation be handled in this approach?**

Microservices can be hosted on Lambda (Serverless), Containers, or can be other Django/Ruby/NodeJS apps.

Front end is via an API Gateway that defines a programmatic interface to the services

Benefits of Rest API based API Gateway are:

- Language agnostic
- Maintains an interface that encapsulates implementation
- Can use SQS to allow queues to invoke APIs
  Need to handle authentication and authorisation for the API
- Use IAM either directly or through API Gateway Resource Policies
- Use Cognito
- Use API keys
- Use an external service through Lambda
