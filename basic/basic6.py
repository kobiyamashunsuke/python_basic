#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import codecs
f=codecs.open('address.txt', 'r',"utf-8")
x=[]
param=sys.argv

count=param[1]

i=0
k=0
for line in f:
	i+=1
        line = line.replace('\n','')
	x.append(line)
	
count1=i-(int(count)+1)

while count1<i-1:
	count1+=1
	print x[count1]



