
import os
import pandas as pd
import shutil
import re
import filetype


B_path =r'\\vumc.nl\onderzoek$\MDL-Artificial-Intelligence\- BEELDMATERIAAL -\Alle videos\Neo frames uit retrovideo(cap) voor delineatie\AA Geselecteerd\Corresponderende images'
A_path = r'\\vumc.nl\onderzoek$\MDL-Artificial-Intelligence\- BEELDMATERIAAL -\Alle videos\Neo frames uit level(cap)videos voor delineatie\Geselecteerde frames + corresponderende images\Corresponderende images'


Destination_path = r'\\vumc.nl\onderzoek$\MDL-Artificial-Intelligence\- BEELDMATERIAAL -\Alle videos\Neo frames uit retrovideo(cap) voor delineatie\AA Geselecteerd\Unieke corresponderende images'

A_files = []



for folderName, subfolders, filenames in os.walk(A_path):
    for file in filenames:
        A_files.append(file)

for folderName, subfolders, filenames in os.walk(B_path):
    for file in filenames:
        if file not in A_files:
            shutil.copy(os.path.join(folderName, file), os.path.join(Destination_path, file))
    
            
