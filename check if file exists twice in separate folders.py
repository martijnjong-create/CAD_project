
import os
import pandas as pd
import shutil
import re
import filetype
''']'''

def walklevel(some_dir, level=1):
    some_dir = some_dir.rstrip(os.path.sep)
    assert os.path.isdir(some_dir)
    num_sep = some_dir.count(os.path.sep)
    for root, dirs, files in os.walk(some_dir):
        yield root, dirs, files
        num_sep_this = root.count(os.path.sep)
        if num_sep + level <= num_sep_this:
            del dirs[:]

extensions = []

image_extensions = ['tif', 'jpg', 'png', 'bmp']
video_extensions = ['mp4', 'mpg']

jelmer_path = r'Z:\- BEELDMATERIAAL -\NDBE image pre-processing\Retrospective\Jelmer\Goed'
main_path = r'Z:\- BEELDMATERIAAL -\Centra\Amsterdam UMC\Retrospectief'

paths = [jelmer_path, main_path]

jelmer_images = []
main_images = []

imagelists = [jelmer_images]

destination_path = r'Z:\- BEELDMATERIAAL -\NDBE image pre-processing\Retrospective\Missing files jelmer'



for folderName, subfolders, filenames in os.walk(main_path):
    for file in filenames:
        if 'amc' in file:
            if 'ndbe' in file:
                file = file.split('.')[0]
                main_images.append(file)
print(main_images)
                
for folderName, subfolders, filenames in os.walk(jelmer_path):
    for file in filenames:
        t_file = file.split('.')[0]
        if 'amc' in t_file:
            if t_file not in main_images:
                print(file)
                #print('missing file found: '+ file)
                #original = os.path.join(folderName, file)
                #target = os.path.join(destination_path, file)
                #shutil.copyfile(original, target)






