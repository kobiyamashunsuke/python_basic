#!/usr/bin/env python

fin1=open('col1.txt', 'r')
fin2=open('col2.txt', 'r')

i=0
n=0
x,y,z=[],[],[]
for line in fin1:
    i+=1
    line = line.replace('\n','')
    x.append(line+'\t')
for line1 in fin2:
    line1=line1.replace('\n','')
    #line1.strip('\n')
    y.append(line1)	
	
for n in range(i):
    data=x[n]+y[n]
    z.append(data)
	
for n in range(i):
	print z[n]
	
fin1.close()
fin2.close()
	
