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