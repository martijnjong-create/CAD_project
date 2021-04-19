#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 16:49:52 2020

@author: macbookpro
"""

# Takes excel file with frames a rows. In the collumn 'Pred' 0 indicates informative, 1,2,3 are non informative categories. 
# Creates progressbar for video. 

from PIL import Image
import pandas as pd

# Read excelfile into dataframe
df = pd.read_excel('excelfile')

# Create green progress bar (length = 10 pixels per frame)
im= Image.new("RGB", (len(df.Pred)*72, 200), "green")

# Iterate over every row 
for index, row in df.iterrows():
    
    # If prediction is not informative, make corresponding pixels red
    if row["Pred"] != 0:
        num = ((index*72), 0, (index*72+72), 200)
        im.paste(("red"), num)

im.show()
im.save()
