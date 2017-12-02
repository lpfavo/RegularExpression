# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 09:52:51 2017

@author: lpfavo231
"""

'''
import re
afile=open('2.txt')
try:
    asd=afile.read()
finally:
    afile.close()
print(1+1)
result = re.findall("(\"+)(.*)(\"+)", asd)
print(result)
for each in result:
    print(each)
'''
'''
import re
gettext1=open("Sthe old man and the sea.txt")
try:
    zxc=gettext1.read()
finally:
    gettext1.close()
getting1=re.findall("[A-Z]+[a-z]*",zxc)
count1=0;
for i in getting1:
    print(i)
    count1+=1
print(count1)
'''

import re
gettext1=open("the old man and the sea.txt")
try:
    zxc=gettext1.read()
finally:
    gettext1.close()
getting1=re.findall("[A-Za-z\-]*ed",zxc)
getting2= re.findall("[A-Za-z\-]*ing",zxc)
#getting3=re.findall("[0-9]{4}",zxc)
getting4= re.findall("[A-Za-z\-]*ly",zxc)
getting3=re.findall("[0-9]{4}",zxc)

gett=re.findall("[]",zxc)
for i in getting1:
    print(i)

for m in getting3:
    print(m)
