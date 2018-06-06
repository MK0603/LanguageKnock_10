# coding: utf-8

import codecs
ifile = codecs.open('D:\hightemp.txt', 'r','utf-8')

lines=ifile.read()

print(lines.count('\n'))
ifile.close()