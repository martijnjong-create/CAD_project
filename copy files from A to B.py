import os
import pandas as pd
import shutil
import re
import filetype

excelpath = r'\\vumc.nl\onderzoek$\MDL-Artificial-Intelligence\- BEELDMATERIAAL -\Overig\Segmentaties\OlympusSegmentationResults20210630\RP_BW_JB subtiliteit 20-40 percentiel.xlsx'


df = pd.read_excel(excelpath) # can also index sheet by name or fetch all sheets
subtle_images = df['files'].tolist()

subtle_images_v2 = []

path = r'Z:\- BEELDMATERIAAL -\Overig\Segmentaties\OlympusSegmentationResults20210630'
destination = r'Z:\- BEELDMATERIAAL -\QADB test set\Nieuwe selectie obv criteria jacques\20-40 percentiel'

for item in subtle_images:
    new_item = item + '.jpg'
    if 'cap' not in new_item:
        subtle_images_v2.append(new_item)



print(subtle_images_v2)
print(len(subtle_images_v2))

count = 0
for folderName, subfolders, files in os.walk(path):
    files.sort()
    for file in files:

        if file in subtle_images_v2:
            count += 1
            shutil.copy(os.path.join(folderName, file), os.path.join(destination, file))
print(count)
            
        
