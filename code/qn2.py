# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 09:16:10 2022

@author: DELL
"""

file=open("test.txt","r")
d=file.read()
c=0
for x in d:
    if x.isspace():
        c+=1
print("No. of words in test.txt file is",c)