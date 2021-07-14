
import os
import pandas as pd
import shutil
import re
import filetype

def walklevel(some_dir, level=1):
    some_dir = some_dir.rstrip(os.path.sep)
    assert os.path.isdir(some_dir)
    num_sep = some_dir.count(os.path.sep)
    for root, dirs, files in os.walk(some_dir):
        yield root, dirs, files
        num_sep_this = root.count(os.path.sep)
        if num_sep + level <= num_sep_this:
            del dirs[:]


def is_wle_image(filename):
    if filename.split('.')[1].lower() not in image_extensions:
        return False
    if 'wle' in filename and 'image' in filename and 'zoom' not in filename:
        return True
    else:
        return False

def is_patient_folder(subfolder):
    parent_folder = subfolder.split('\\')[-1]
    if IDRegex.search(parent_folder):
        return True
    elif dateRegex.search(parent_folder):
        return True
    else:
        return False


IDRegex = re.compile(r'[\w]{3,4}_(\d)+')
dateRegex = re.compile(r'[\d]{1,2}-[\d]{1,2}-\d\d\d\d')

image_extensions = ['tif', 'jpg', 'png', 'bmp']
video_extensions = ['mp4', 'mpg', 'avi']

A_path = r'\\vumc.nl\onderzoek$\MDL-Artificial-Intelligence\- BEELDMATERIAAL -\Alle videos\Neo frames uit retrovideo(cap) voor delineatie\AA Geselecteerd'
B_path = r'Z:\- BEELDMATERIAAL -\Centra'
destination_path = r'\\vumc.nl\onderzoek$\MDL-Artificial-Intelligence\- BEELDMATERIAAL -\Alle videos\Neo frames uit retrovideo(cap) voor delineatie\AA Geselecteerd\Corresponderende images'

A_images = []
B_subfolders = []

count = 0

for folderName, subfolders, filenames in os.walk(A_path):
    for file in filenames:
        #print(file)
        filename = file.split('.')[0]
        try:
            filename = file.split('_')[0] + '_'+ file.split('_')[1] + '_'+file.split('_')[2] + '_'+file.split('_')[3] + '_'+file.split('_')[4] + '_'+file.split('_')[5] + '_' +file.split('_')[6]+'_' +file.split('_')[7]
            A_images.append(filename)
        except:
            None
        #print(filename)


A_images = list(dict.fromkeys(A_images))
A_images.sort()
for i in A_images:
    print(i)

        
print('DDDDDDDDDDDOOOOOOOOOOOOOOOOONNNNNNNNNNNNNNNNNEEEEEEEEEEEEEE')
                
for folderName, subfolders, filenames in os.walk(B_path):
    for file in filenames:
        t_file = file.split('.')[0]
        if t_file in A_images:
            if is_patient_folder(folderName):
                B_subfolders.append(folderName)
                #print(folderName)
                #print(t_file)

B_subfolders = list(dict.fromkeys(B_subfolders))
for i in B_subfolders:
    print(i)



print('DDDDDDDDDDDOOOOOOOOOOOOOOOOONNNNNNNNNNNNNNNNNEEEEEEEEEEEEEE')  

for path_to_folder in B_subfolders:
    for folderName, subfolders, filenames in walklevel(path_to_folder, level=0):
        for file in filenames:

            if is_wle_image(file):
                print(file)
                #shutil.copy(os.path.join(folderName, file), os.path.join(destination_path, file))
                    







