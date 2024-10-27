# ALB (Lab 5)
**Steps to create an ALB for EC2 instances in two different availability zones**:

1. create and configure security group by authorising inbound traffic for SSH and HTTP.
2. get availability zones in the region
3. create a key pair
4. create EC2 instances by specifying instance type, security group and availability zones
5. get available subnets in the region
6. create a load balancer by specifying name, subnets, security group, scheme (internet-facing or internal), IP address type (IPv4 or dualstack).
7. create and configure target group by specifying name, protocol (HTTP), port (80), vpc id, port to use for health check, target type.
8. register targets for the configured target group.
9. create and configure listener by specifying load balancer arn, protocol, port, and action (forward HTTP requests to the target group)

**Steps to test the ALB**:
1. ssh into EC2 instance (establish secure shell connection)
2. update instance and install apache2 (web server software)
3. edited HTML tags of the default Apache web page
4. accessed instance by their public IP address in browser


# Web Application (Lab 6)
**Steps to set up load balancer to Django application:**
1. create an EC2 instance by specifying instance type, security group and availability zones, and ssh into the instance
2. install virtual environment package, set up a virtual environment, activate the virtual environment
3. install django, create a django project and create a django app
4. install nginx and configure nginx, restart nginx
5. edit Django files (views.py and urls.py)
6. run the web server and access the app through the EC2 instance's public IP address
7. create an ALB by specifying name, subnets, security group, scheme (internet-facing or internal), IP address type (IPv4 or dualstack).
8. create and configure target group by specifying name, protocol to use (HTTP), port to forward traffic (80), vpc id, port to use for health check, health check interval, health check path, target type.
9.  register targets for the configured target group
10. create and configure listener by specifying load balancer arn, protocol, port, and action (forward HTTP requests to the target group)


# Devops (lab 7)
**Use Fabric to automate the setup of a Python 3 virtual environment, nginx and a Django app within the EC2 instance we created**:
1. create and configure a security group
2. create an EC2 instance
3. install Fabric and create a config file in ~/.ssh
4. connect to the EC2 instance and automate the setup of Python3 virtual env, nginx, and a Django app within the EC2 instance
5. install virtual environment package, set up a virtual environment, activate the virtual environment
6. install django, create a django project and create a django app
7. install nginx and configure nginx, restart nginx
8. edit Django files (views.py and urls.py)
9. run the web server and access the app through the EC2 instance's public IP address


# AI/Comprehend/Rekognition (Lab 9)
**Entities**: pieces of information extracted from texts. They are _objects, concepts, or categories_ such as places, organisations, names, dates, and quantities. For example, "Sam was born in France," "Sam" is a person, "France" is location. These are entities in this sentence.

**Keyphrases**: meaningful *pieces of text* that capture the *main ideas* of a paragraph or article. They are generally nouns, verbs or phrases that summarise key concepts or central topics in the text. For example, in a sentence about cats' daily routine, the key phrases might be "cat", "sleep", "eat", "play" and "grooming".

**Syntaxes**: the rules of how words are arranged to form sentences. It is about the structure of sentences and determines how different parts of speech, e.g. nouns, verbs, pronouns and adjectives combine to convey clear messages. For example, in the sentence "The cat is cute", "cat" is the subject, "is" is the verb, "cute" is the adjective. This sentence follows the basic structure "subject + linking verb + predicate adjective".

**How to use Rekognition**:
- create S3 bucket and upload images to it
- perform operations like detect_labels, detect_moderation_labels, detect_faces, detect_text.

s3.upload_file(Filename, Bucket, Key): (local file path, bucket name, destination path in S3)

