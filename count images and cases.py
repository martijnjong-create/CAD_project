
import os
import pandas as pd
import shutil
import re
import filetype



image_extensions = ['tif', 'jpg', 'png', 'bmp']
video_extensions = ['mp4', 'mpg', 'avi']


path = r'Z:\- BEELDMATERIAAL -\QADB test set\Preliminary test set\ndbe alternatief'

IDs = {}

for folderName, subfolders, files in os.walk(path):
    files.sort()
    for file in files:
        ID = file.split('_')[0] + file.split('_')[1]
        if ID in IDs:
            
            IDs[ID] +=1
        else:

            IDs[ID] = 1

print(len(IDs.keys()))
total_delineations = 0
for value in IDs.values():
    total_delineations = total_delineations + value
print(total_delineations)

            


        
        
        





        
    
    
        
            
            
            

            
        


            
  




        
   
