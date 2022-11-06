# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 10:32:44 2022

@author: DELL
"""

from freqwd import wordfreq
dic1=wordfreq("test.txt")

st=""""""
trr="""
<tr>
    <td>word</td>
    <td>freq</td>
</tr>
"""
for i,j in dic1.items():  
    trr1=trr.replace("word",str(i))
    trr1=trr1.replace("freq",str(j))
    st+=trr1
htmltmp="""
<html>
<head>
<title>wordtags</title>
</head>
<body>

  <table style="border-color:green">
      <tr>
          <th>WORDS</th>
          <th>FREQUENCY</th>
      </tr>
      {}
  </table>
</body>
</html>"""
h=htmltmp.replace("{}",st)
f=open("wordtags.html","w")
f.close
f1=open("wordtags.html","w")
f1.write(h)
f1.close