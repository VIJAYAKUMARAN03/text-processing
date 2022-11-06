# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 12:48:52 2022

@author: DELL
"""

from freqwd import wordfreq
dic1=wordfreq("test.txt")
dic1=wordfreq("test.txt")
f=open("test.txt","r")
l=f.readlines()
st=""""""
trr="""
<tr>
    <td class="tooltip">word
        <span class="tooltiptext">PaRa</span>
    </td>
    
</tr>
"""
tll="""<p>bb</p><br>"""

for i,j in dic1.items():
    paras=""""""
    trr1=trr.replace("word",str(i))
    for x in l:
        if i in x:
            t1=tll.replace("bb",x)
            paras+=t1
            #print(i,x)
    trr1=trr1.replace("PaRa",paras)
    st+=trr1
htmltmp="""
<html>
<head>
<title>wordfreqcloud3</title>
<style>
.tooltip {
  position: relative;
  display: inline-block;
  border-bottom: 1px dotted black;
}

.tooltip .tooltiptext {
  visibility: hidden;
  width: 1020px;
  background-color: black;
  color: #fff;
  text-align: center;
  border-radius: 6px;
  padding: 5px 0;

  /* Position the tooltip */
  position: absolute;
  z-index: 1;
}

.tooltip:hover .tooltiptext {
  visibility: visible;
}
</style>
</head>
<body>
  <table style="border-color:green">
      <tr>
          <th>WORDS</th>
      </tr>
      {}
  </table>
</body>
</html>"""
h=htmltmp.replace("{}",st)
f=open("wordfreqcloud3.html","w")
f.close
f1=open("wordfreqcloud3.html","w")
f1.write(h)
f1.close
