# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 09:21:11 2022

@author: DELL
"""

file1=open("test.txt","r")
file2=open("noise.txt","r")
f1=file1.read()
f2=file2.read()
l1=list(f1.split())
l2=list(f2.split())
for x in l1:
    if x not in l2:
        print(x,end=" ")