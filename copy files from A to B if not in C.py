import os
import pandas as pd
import shutil
import re
import filetype



path = r'Z:\- BEELDMATERIAAL -\QADB data voor tim 110721\Neo\Test'
path2 = r'Z:\- BEELDMATERIAAL -\QADB data voor tim 110721\Neo\Train'
destination = r'Z:\- BEELDMATERIAAL -\QADB data voor tim 110721\Neo\Test 2'

stored_files = []

for folderName, subfolders, files in os.walk(path):
    files.sort()
    for file in files:
        if 'Thumbs' in file:
            continue
        actual_file = file.split('.')[0]
        stored_files.append(actual_file)

stored_files = list(dict.fromkeys(stored_files))
print(len(stored_files))


for folderName, subfolders, files in os.walk(path2):
    files.sort()
    for file in files:
        actual_file = file.split('.')[0]
        if actual_file in stored_files:
            shutil.copy(os.path.join(folderName, file), os.path.join(destination, file))
            print(file)
        
