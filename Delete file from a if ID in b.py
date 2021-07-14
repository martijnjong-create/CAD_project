import os
import pandas as pd
import shutil
import re
import filetype



path = r'Z:\- BEELDMATERIAAL -\QADB data voor tim 110721\Neo\Test'
path2 = r'Z:\- BEELDMATERIAAL -\QADB data voor tim 110721\Neo\Train'
destination = r'Z:\- BEELDMATERIAAL -\QADB test set\Nieuwe selectie obv criteria jacques\20-40 percentiel\Geselecteerd\Reserve\Zonder delineatie'

stored_IDs = []

for folderName, subfolders, files in os.walk(path):
    files.sort()
    for file in files:
        ID = file.split('_')[0] + '_' + file.split('_')[1]
        stored_IDs.append(ID)

stored_IDs = list(dict.fromkeys(stored_IDs))
print(len(stored_IDs))
print(stored_IDs)


for folderName, subfolders, files in os.walk(path2):
    files.sort()
    for file in files:
        ID = file.split('_')[0] + '_' + file.split('_')[1]
        if ID in stored_IDs:
            print('delete')
            #os.remove(os.path.join(folderName, file))
        
        
