import os
import filetype


techniques = ['zoom', 'zoomimage', 'closebyimage', 'closebyvideo']
pathologies = ['neo', 'ndbe', 'lgd']

count_dict = {}

for technique in techniques:
    for pathology in pathologies:
        count_dict[pathology + '_'+ technique] = 0


extensions = ['tif', 'jpg', 'png', 'bmp', 'mp4', 'mpg', 'avi']

path = r'Z:\- BEELDMATERIAAL -\All NBI zoom data (conform inclusie criteria)'
for folderName, subfolders, filenames in os.walk(path):
    for file in filenames:
        print(file)
        filepath = os.path.join(folderName, file)
        kind = filetype.guess(filepath)
        
        if kind == None:
            continue
        extension = kind.extension
        if extension not in extensions:
            continue
        pathology = file.split('_')[4]
        if pathology == 'eac' or pathology == 'hgd':
            pathology = 'neo'
        technique = file.split('_')[3]
        
        count_dict[pathology + '_'+ technique] += 1
                    
print(count_dict)
for item in count_dict.items():
    print(item)
