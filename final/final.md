
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
