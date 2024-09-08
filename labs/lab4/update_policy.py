import boto3
import json

# Initialise the KMS client
kms = boto3.client("kms")

# Replace with your student number and username
student_number = "22756463"
alias_name = f"alias/{student_number}"

# Create a KMS key
try:
    response = kms.create_key(
        Description="KMS key for student number",
        KeyUsage="ENCRYPT_DECRYPT",  # Key usage can be 'ENCRYPT_DECRYPT' for most cases
    )
    key_id = response["KeyMetadata"]["KeyId"]
    print(f"KMS Key created with KeyId: {key_id}")
except Exception as e:
    print(f"Error creating KMS key: {e}")

# Check if alias already exists and delete it
try:
    response = kms.list_aliases()
    for alias in response['Aliases']:
        if alias['AliasName'] == alias_name:
            # If the alias exists, delete it
            print(f"Alias {alias_name} already exists. Deleting it.")
            kms.delete_alias(AliasName=alias_name)
            break
except Exception as e:
    print(f"Error checking or deleting existing alias: {e}")

# Create an alias for the KMS key
try:
    kms.create_alias(AliasName=alias_name, TargetKeyId=key_id)
    print(f"Alias '{alias_name}' created for KMS KeyId: {key_id}")
except Exception as e:
    print(f"Error creating alias: {e}")

# Attach a policy to the KMS key
try:
    # Define the key policy
    key_policy = {
        "Version": "2012-10-17",
        "Id": "key-consolepolicy-3",
        "Statement": [
            {
                "Sid": "Enable IAM User Permissions",
                "Effect": "Allow",
                "Principal": {"AWS": "arn:aws:iam::489389878001:root"},
                "Action": "kms:*",
                "Resource": "*",
            },
            {
                "Sid": "Allow access for Key Administrators",
                "Effect": "Allow",
                "Principal": {"AWS": "arn:aws:iam::489389878001:user/22756463@student.uwa.edu.au"},
                "Action": [
                    "kms:Create*",
                    "kms:Describe*",
                    "kms:Enable*",
                    "kms:List*",
                    "kms:Put*",
                    "kms:Update*",
                    "kms:Revoke*",
                    "kms:Disable*",
                    "kms:Get*",
                    "kms:Delete*",
                    "kms:TagResource",
                    "kms:UntagResource",
                    "kms:ScheduleKeyDeletion",
                    "kms:CancelKeyDeletion",
                ],
                "Resource": "*",
            },
            {
                "Sid": "Allow use of the key",
                "Effect": "Allow",
                "Principal": {"AWS": "arn:aws:iam::489389878001:user/22756463@student.uwa.edu.au"},
                "Action": [
                    "kms:Encrypt",
                    "kms:Decrypt",
                    "kms:ReEncrypt*",
                    "kms:GenerateDataKey*",
                    "kms:DescribeKey",
                ],
                "Resource": "*",
            },
            {
                "Sid": "Allow attachment of persistent resources",
                "Effect": "Allow",
                "Principal": {"AWS": "arn:aws:iam::489389878001:user/22756463@student.uwa.edu.au"},
                "Action": ["kms:CreateGrant", "kms:ListGrants", "kms:RevokeGrant"],
                "Resource": "*",
                "Condition": {"Bool": {"kms:GrantIsForAWSResource": "true"}},
            },
        ],
    }

    # Attach the policy to the KMS key
    kms.put_key_policy(
        KeyId=key_id,
        PolicyName="default",
        Policy=json.dumps(key_policy),  # Convert the policy dictionary to a JSON string
    )
    print(f"Key policy attached to KMS KeyId: {key_id}")
except Exception as e:
    print(f"Error attaching key policy: {e}")
