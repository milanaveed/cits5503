import os
import boto3

# Initialize the S3 client
s3 = boto3.client('s3')

# Define your S3 bucket name
BUCKET_NAME = '22756463-cloudstorage'  
LOCAL_ROOT_DIR = './restored_files'  


for object in s3.list_objects(Bucket = BUCKET_NAME)['Contents']:
    object_key = object['Key']
    print("Downloading %s" % object_key)
    cloud_dir_path = os.path.dirname(object_key)
    local_dir_path = os.path.join(LOCAL_ROOT_DIR, cloud_dir_path)
    if not os.path.exists(local_dir_path):
        os.makedirs(local_dir_path)
    local_file_path = os.path.join(LOCAL_ROOT_DIR, object_key)
    s3.download_file(BUCKET_NAME, object_key, local_file_path)




# def download_file(s3_bucket, s3_key, local_file_path):
#     """Downloads an individual file from S3 to a local directory."""
#     try:
#         print(f"Downloading {s3_key} to {local_file_path}")
#         # Create the directories if they don't exist
#         os.makedirs(os.path.dirname(local_file_path), exist_ok=True)
#         # Download the file
#         s3.download_file(s3_bucket, s3_key, local_file_path)
#         print(f"Successfully downloaded {s3_key}")
#     except Exception as e:
#         print(f"Failed to download {s3_key}: {str(e)}")

# def restore_from_s3(bucket_name, local_root_dir):
#     """Restores the files from the given S3 bucket to the local directory structure."""
#     try:
#         # List the objects in the bucket
#         response = s3.list_objects_v2(Bucket=bucket_name)
        
#         if 'Contents' not in response:
#             print(f"No files found in bucket {bucket_name}.")
#             return
        
#         # Iterate over the files in the bucket
#         for obj in response['Contents']:
#             s3_key = obj['Key']
#             # Define the local path relative to the root directory
#             local_file_path = os.path.join(local_root_dir, s3_key)
            
#             # Download the file from S3
#             download_file(bucket_name, s3_key, local_file_path)

#     except Exception as e:
#         print(f"Error occurred while restoring files: {str(e)}")

# if __name__ == "__main__":
#     # Create the root directory if it doesn't exist
#     if not os.path.exists(LOCAL_ROOT_DIR):
#         os.makedirs(LOCAL_ROOT_DIR)
    
#     # Restore files from the S3 bucket to the local directory
#     restore_from_s3(BUCKET_NAME, LOCAL_ROOT_DIR)
#     print("Restoration completed.")
