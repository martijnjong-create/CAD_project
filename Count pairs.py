import shutil
import filetype
import os
import pandas as pd

def remove_thumbs(dir_list):
    if 'Thumbs.db' in dir_list:
        dir_list.remove('Thumbs.db')
    return dir_list

image_extensions = ['tif', 'jpg', 'png', 'bmp']
video_extensions = ['mp4', 'mpg', 'avi']




countlist = []

path = r'\\vumc.nl\onderzoek$\MDL-Artificial-Intelligence\- BEELDMATERIAAL -\Centra\Amsterdam UMC\Prospectief'
IDs = {}
subfolders = []

for folderName, subfolders, files in os.walk(path):
    subfolders.sort()
    files.sort()
    files = remove_thumbs(files)
    for file in files:
        
        if 'PAIRS' in folderName:
            root = folderName.split('PAIRS\\')[1]
            countlist.append(os.path.join(root, file))
print(countlist)

pair_list = []
ID_list = []
pathology_list = []
# split countlist in separate lists  CAP vs NO CAP\\amc1081
for item in countlist:

    if 'ndbe' in item:
        pathology = 'ndbe'
    elif 'eac' in item or 'hgd' in item:
        pathology = 'neo'
    else:
        pathology = 'unknown'
        print(item)

    item = item.split('_')[0] + item.split('_')[1]
    pair_list.append(item.split('\\')[0])
    ID_list.append(item.split('\\')[1])
    pathology_list.append(pathology)



# make dataframe, each image and video will have 1 row. Columns are categories of properties of video/image.
output_df = pd.DataFrame(list(zip(pair_list,pathology_list, ID_list)), columns = ['Pair','Pathology', 'ID'])
print(output_df)




# create dataframe for case counting
ID_output_df = output_df
ID_output_df = ID_output_df.drop_duplicates()



output_df = pd.crosstab([output_df.Pair], [output_df.Pathology],
                            rownames = ['Pair'], colnames = ['Pathology -> '], dropna = True)

ID_output_df = pd.crosstab([ID_output_df.Pair], [ID_output_df.Pathology],
                            rownames = ['Pair'], colnames = ['Pathology -> '], dropna = True)
ID_output_df = ID_output_df.add_suffix(' patients')

# Merge both dataframes
complete_df = pd.concat([output_df, ID_output_df], axis=1)
complete_df = complete_df[[item for items in zip(output_df.columns, ID_output_df.columns) for item in items]]

complete_df.to_excel('pair_count.xlsx')

#output_df.to_excel('pair_total_count.xlsx')
#ID_output_df.to_excel('pair_case_count.xlsx')




        
