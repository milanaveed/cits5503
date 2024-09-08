# Reference: https://github.com/zhangzhics/CITS5503_Sem2/blob/master/Labs/src/fileencrypt.py
import os, random, struct
from Crypto.Cipher import AES
from Crypto import Random
import boto3
import base64
import hashlib

BLOCK_SIZE = 16
CHUNK_SIZE = 64 * 1024

s3 = boto3.client('s3')

bucket_name = '22756463-cloudstorage'  # S3 bucket name
local_directory = './restored_files1'  # Local directory to store files obtained from cloud


# Download files from S3 bucket to local directory
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


def encrypt_file(password, in_filename, out_filename):

    key = hashlib.sha256(password.encode("utf-8")).digest()

    iv = Random.new().read(AES.block_size)
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    filesize = os.path.getsize(in_filename)

    with open(in_filename, 'rb') as infile:
        with open(out_filename, 'wb') as outfile:
            outfile.write(struct.pack('<Q', filesize))
            outfile.write(iv)

            while True:
                chunk = infile.read(CHUNK_SIZE)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += ' '.encode("utf-8") * (16 - len(chunk) % 16)

                outfile.write(encryptor.encrypt(chunk))


def decrypt_file(password, in_filename, out_filename):

    key = hashlib.sha256(password.encode("utf-8")).digest()

    with open(in_filename, 'rb') as infile:
        origsize = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]
        iv = infile.read(16)
        decryptor = AES.new(key, AES.MODE_CBC, iv)

        with open(out_filename, 'wb') as outfile:
            while True:
                chunk = infile.read(CHUNK_SIZE)
                if len(chunk) == 0:
                    break
                outfile.write(decryptor.decrypt(chunk))

            outfile.truncate(origsize)


# Main program
password = 'cat is cuteee'

# Download the files from the S3 bucket
download_s3_files(bucket_name, local_directory)

# Encrypt and decrypt the files
for dir_name, subdir_list, file_list in os.walk(local_directory, topdown=True):
    if dir_name != local_directory:
        for fname in file_list:
            print(fname)
            file_path = os.path.join(dir_name, fname)

            # Encrypt the file
            encrypt_file(password, file_path, out_filename=f"{file_path}.enc")

            # Decrypt the encrypted file
            decrypt_file(password, f"{file_path}.enc", out_filename=f"{file_path}.dec")
