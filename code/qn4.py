# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 09:32:13 2022

@author: DELL
"""

import pandas as pd
from freqwd import wordfreq

dic = wordfreq("test.txt")
t=pd.DataFrame(dic.items(),columns=["WORDS","FREQUENCY"]) 
print(t.to_string())