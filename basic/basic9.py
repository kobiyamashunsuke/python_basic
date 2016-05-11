#-*- coding: utf-8 -*-
f=open('address.txt','r')
from operator import itemgetter
x1,x2,y1,y2,z1,z2=[],[],[],[],[],[]
i=0
for line in f:
        i+=1
	line=line.expandtabs(1)
        line=line.replace('\n','')
	data1=line.split(' ')
	x1.append(data1[0]+'\n')
	y1.append(data1[1]+'\t')

for n in range(i):
    data1=y1[n]+x1[n]
    z1.append(data1)

lines=sorted(z1)

for line in lines:
    line=line.expandtabs(1)
    line=line.replace('\n','')
    data2=line.split(' ')
    y2.append(data2[0]+'\n')
    x2.append(data2[1]+'\t')

for n in range(i):
    data2=x2[n]+y2[n]
    data2=data2.replace('\n','')
    z2.append(data2)

lines2=sorted(z2)
for n in range(i):
    print z2[n]
f.close()

