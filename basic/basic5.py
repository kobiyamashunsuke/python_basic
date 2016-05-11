#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import codecs
f=codecs.open('address.txt', 'r',"utf-8")
x=[]
param=sys.argv

count=param[1]

##print count

for line in f:
        line = line.replace('\n','')
	x.append(line)
	
for n in range(int(count)):
	print x[n]



