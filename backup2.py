#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      rsparano
#
# Created:     21/12/2019
# Copyright:   (c) rsparano 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os
import zipfile
import shutil

# copy files and folder and compress into a zip file

def doprocess(source_folder, target_zip):
    zipf = zipfile.ZipFile(target_zip, "w")
    for subdir, dirs, files in os.walk(source_folder):
        for file in files:
            print (os.path.join(subdir, file))
            zipf.write(os.path.join(subdir,file))

    print ("Created ", target_zip)

#Copy files to a target folder
def docopy(source_folder, target_folder):
    for subdir, dirs, files in os.walk(source_folder):
        for file in files:
            print (os.path.join(subdir, file))
            shutil.copy2(os.path.join(subdir, file),target_folder)


if __name__ == '__main__':
    print ('Starting Execution')

    #Copy to backup folder
    source_folder = 'C:\\Temp'
    target_folder = 'C:\\Users\\rsparano\\Desktop\\Backups'
    docopy(source_folder,target_folder)

    #Copy to zip
    source_folder = 'C:\\Temp'
    target_zip = 'C:\\Users\\rsparano\\Desktop\\Backups\\DummyZip.zip'
    doprocess(source_folder,target_zip)

