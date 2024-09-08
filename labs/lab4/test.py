#####################TEST#####################
import os

local_directory = './restored_files'

def main():

    # Encrypt and decrypt the files
    for dir_name, subdir_list, file_list in os.walk(local_directory, topdown=True):
        print(dir_name)
        if dir_name != local_directory:
            for fname in file_list:
                print(fname)
                file_path = os.path.join(dir_name, fname)

                # # Encrypt the file
                # encrypted_file_path = encrypt_file(file_path, key_id)

                # # Decrypt the encrypted file
                # decrypt_file(encrypted_file_path)

if __name__ == "__main__":
    main()
