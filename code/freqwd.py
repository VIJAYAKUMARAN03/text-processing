# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 10:10:13 2022

@author: DELL
"""


def wordfreq(s):
    f1=open(s,"r")
    r=f1.read()
    l1=list(r.split())
    l=[]
    dic={}
    for x in l1:
        if(x[-1]==',' or x[-1]=='.' or x[-1]=='"' or x[-1]==';'):
            x=x[:-1]
        elif(x[0]==',' or x[0]=='.' or x[0]=='"' or x[0]==';'):
            x=x[1:]
        l.append(x)
    for i in l:
        if i not in dic.keys():
            dic[i]=1
        else:
            dic[i]=dic[i]+1
    return dic