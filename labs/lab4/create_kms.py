import boto3

# Initialise the KMS client
kms = boto3.client('kms')

student_number = '22756463'


# Create a KMS key
try:
    response = kms.create_key(
        Description="KMS key for student number",
        KeyUsage='ENCRYPT_DECRYPT',  # Key usage can be 'ENCRYPT_DECRYPT' for most cases
        # Origin='AWS_KMS'  # Specifies AWS to manage key material
    )
    key_id = response['KeyMetadata']['KeyId']
    print(f"KMS Key created with KeyId: {key_id}")
except Exception as e:
    print(f"Error creating KMS key: {e}")


# Create an alias for the KMS key
try:
    alias_name = f'alias/{student_number}'
    kms.create_alias(
        AliasName=alias_name,
        TargetKeyId=key_id
    )
    print(f"Alias '{alias_name}' created for KMS KeyId: {key_id}")
except Exception as e:
    print(f"Error creating alias: {e}")

