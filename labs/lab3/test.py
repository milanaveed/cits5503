import os

ROOT_DIR = '.'


# parse directory and upload files
for dir_name, subdir_list, file_list in os.walk(ROOT_DIR, topdown=True):
    print(dir_name)
    if dir_name != ROOT_DIR:
        for fname in file_list:
            print(fname)
            # upload_file("%s/" % dir_name[2:], "%s/%s" % (dir_name, fname), fname)