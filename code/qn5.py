# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 09:38:30 2022

@author: DELL
"""

import pandas as pd
from freqwd import wordfreq

dic1=wordfreq("test.txt")
file2=open("noise.txt","r")
f2=file2.read()
l2=list(f2.split())
dic2={}
for i,j in dic1.items():
    if i not in l2:
        dic2[i]=j
t=pd.DataFrame(dic2.items(),columns=["WORDS","FREQUENCY"]) 
print(t.to_string())