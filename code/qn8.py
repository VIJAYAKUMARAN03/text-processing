# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 11:34:20 2022

@author: DELL
"""


from freqwd import wordfreq
dic1=wordfreq("test.txt")
st=""""""
trr="""
<tr>
    <td class="tooltip">word
        <span class="tooltiptext">Tool</span>
    </td>
    
</tr>
"""
for i,j in dic1.items():  
    trr1=trr.replace("word",str(i))
    trr1=trr1.replace("Tool","frequency is "+str(j))
    st+=trr1
htmltmp="""
<html>
<head>
<title>wordfreqcloud2</title>
<style>
.tooltip {
  position: relative;
  display: inline-block;
  border-bottom: 1px dotted black;
}

.tooltip .tooltiptext {
  visibility: hidden;
  width: 120px;
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
f=open("wordfreqcloud2.html","w")
f.close
f1=open("wordfreqcloud2.html","w")
f1.write(h)
f1.close
