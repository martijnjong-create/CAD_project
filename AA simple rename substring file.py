import shutil
import os


count = 0

path = r'Z:\- BEELDMATERIAAL -\Centra\Amsterdam UMC\Prospectief\amc_237'
images = ['png', 'tiff', 'jpg', 'bmp']
for folderName, subfolders, filenames in os.walk(path):
    
    for file in filenames:
        print(file)
        if '.jpg' in file:

            #os.rename(os.path.join(folderName, file), os.path.join(folderName, file.replace('eac', 'hgd')))
       
