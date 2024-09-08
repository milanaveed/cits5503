import boto3
import os

# Initialise the clients
kms = boto3.client('kms')
s3 = boto3.client('s3')

bucket_name = '22756463-cloudstorage'  # S3 bucket name
key_id = 'a9b69f17-c23c-4fa8-ba73-a20940e141aa'  # KMS Key ID
local_directory = './restored_files'  # Local directory to store files obtained from cloud

# Step 1: Download files from S3 bucket to local directory
def download_s3_files(bucket_name, local_directory):
    if not os.path.exists(local_directory):
        os.makedirs(local_directory)

    # List files in the S3 bucket
    objects = s3.list_objects_v2(Bucket=bucket_name)

    if 'Contents' in objects:
        for obj in objects['Contents']:
            file_key = obj['Key']
            file_path = os.path.join(local_directory, file_key)

            # Create subdirectories if necessary
            os.makedirs(os.path.dirname(file_path), exist_ok=True)

            # Download the file from S3 to local directory
            s3.download_file(bucket_name, file_key, file_path)
            print(f"Downloaded {file_key} to {file_path}")
    else:
        print("No files found in the S3 bucket.")

# Step 2: Encrypt the file using KMS
def encrypt_file(file_path, key_id):
    with open(file_path, 'rb') as file:
        file_data = file.read()

    # Encrypt the data using KMS
    encrypted_data = kms.encrypt(KeyId=key_id, Plaintext=file_data)['CiphertextBlob']

    # Write the encrypted data to a new file
    encrypted_file_path = f"{file_path}.encrypted"
    with open(encrypted_file_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)

    print(f"Encrypted file written to {encrypted_file_path}")
    return encrypted_file_path

# Step 3: Decrypt the encrypted file using KMS
def decrypt_file(encrypted_file_path):
    with open(encrypted_file_path, 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()

    # Decrypt the data using KMS
    decrypted_data = kms.decrypt(CiphertextBlob=encrypted_data)['Plaintext']

    # Write the decrypted data to a new file
    decrypted_file_path = f"{encrypted_file_path}.decrypted"
    with open(decrypted_file_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)

    print(f"Decrypted file written to {decrypted_file_path}")
    return decrypted_file_path


def main():
    # Download the files from the S3 bucket
    download_s3_files(bucket_name, local_directory)

    # Encrypt and decrypt the files
    for dir_name, subdir_list, file_list in os.walk(local_directory, topdown=True):
        if dir_name != local_directory:
            for fname in file_list:
                print(fname)
                file_path = os.path.join(dir_name, fname)

                # Encrypt the file
                encrypted_file_path = encrypt_file(file_path, key_id)

                # Decrypt the encrypted file
                decrypt_file(encrypted_file_path)

if __name__ == "__main__":
    main()