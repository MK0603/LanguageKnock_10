# coding: utf-8

import codecs
import re
ifile = codecs.open('D:\hightemp.txt', 'r','utf-8')

lines=ifile.read()
ifile.close()
reg=re.findall('.$', lines, re.MULTILINE)

print(len(reg))
#print(lines.count('\n'))
