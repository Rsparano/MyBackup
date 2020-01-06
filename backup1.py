#-------------------------------------------------------------------------------
# Name:        backup1
# Purpose:
#
# Author:      rsparano
#
# Created:     12/21/2019
# Copyright:   (c) rsparano 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import datetime
import os
import shutil

#GOOGLE_DRIVE_DIRECTORY = 'C:\\Users\\rsparano\\OneDrive\\Dev1Backup'
SOURCE_DIRECTORY='C:\\Temp'
MAIN_BACKUP_DIRECTORY = 'C:\\Users\\rsparano\\Desktop\\Backups\\Dev1_backup_{0}'
EXTERNAL_DRIVE_DIRECTORY = 'C:\\Backup\\Local\\Dev1_backup_{0}'

def get_backup_directory(base_directory):
    date = str(datetime.datetime.now())[:16]
    date = date.replace(' ', '_').replace(':', '')
    return base_directory.format(date)

def copy_files(directory):
    for subdir, dir, files in os.walk(SOURCE_DIRECTORY):
        print (subdir, dir, files)
        for item in files:
             print (item)
             file_path = os.path.join(SOURCE_DIRECTORY, item)
             shutil.copy2(file_path, directory)
             print (file_path)
'''    if os.path.isfile(file_path):
                shutil.copy(file_path, directory)
        for file in SOURCE_DIRECTORY:
            print (file)
'''
def perform_backup(base_directory):
    backup_directory = get_backup_directory(base_directory)
    os.makedirs(backup_directory)
    copy_files(backup_directory)

def main():
    perform_backup(MAIN_BACKUP_DIRECTORY)
    perform_backup(EXTERNAL_DRIVE_DIRECTORY)

if __name__ == '__main__':
    main()
