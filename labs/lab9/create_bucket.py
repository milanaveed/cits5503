import os
import boto3

ROOT_DIR = '.'
ROOT_S3_DIR = '22756463-cloudstorage-lab9'

s3 = boto3.client("s3")

bucket_region = 'us-east-1'

bucket_config = {'LocationConstraint': bucket_region} 


def upload_file(folder_name, file, file_name):
    print("Uploading %s" % file)

    try:
        s3.upload_file(file, ROOT_S3_DIR, folder_name+file_name)
    except Exception as error:
        print(error)
        pass

def main():
    try:
        # Check if bucket exists
        s3.head_bucket(Bucket=ROOT_S3_DIR)
        print(f"Bucket {ROOT_S3_DIR} already exists.")
    except Exception as error:
        # If bucket does not exist, create it
        print(f"Creating bucket {ROOT_S3_DIR}...")
        try:
            if bucket_region == 'us-east-1':
                # us-east-1 (N. Virginia) does not require LocationConstraint
                s3.create_bucket(Bucket=ROOT_S3_DIR)
                print(f"Bucket {ROOT_S3_DIR} created successfully.")
            else:
                response = s3.create_bucket(
                    Bucket=ROOT_S3_DIR,
                    CreateBucketConfiguration=bucket_config
                )
                print(f"Bucket {ROOT_S3_DIR} created successfully.")
        except Exception as error:
            print(f"Error creating bucket: {str(error)}")
            raise

    # parse directory and upload files
    for dir_name, subdir_list, file_list in os.walk(ROOT_DIR, topdown=True):
        if dir_name != ROOT_DIR:
            for fname in file_list:
                upload_file("%s/" % dir_name[2:], "%s/%s" % (dir_name, fname), fname)

    print("done")

if __name__ == "__main__":
    main()