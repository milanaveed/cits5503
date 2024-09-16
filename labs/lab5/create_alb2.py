import boto3
from botocore.exceptions import ClientError

# Create a Boto3 EC2 and ELBv2 client
ec2 = boto3.client('ec2')
elbv2 = boto3.client('elbv2')


instance_id = 'i-04cdb45522154b089'
target_group_arn = 'arn:aws:elasticloadbalancing:us-east-1:489389878001:targetgroup/22756463-target-group/3b319eeca9dc91b5'


# Step 9: Register targets (EC2 instances) to the target group
def register_target(target_group_arn, instance_id):
    try:
        targets = [{'Id': instance_id}]
        elbv2.register_targets(
            TargetGroupArn=target_group_arn,
            Targets=targets
        )
        print(f"Registered instances {instance_id} to the target group.")
    except ClientError as e:
        print(f"Error registering targets: {e}")


# Step 9: Register EC2 instances as targets
register_target(target_group_arn, instance_id)