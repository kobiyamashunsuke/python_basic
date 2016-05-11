#!/user/bin/env python

x,y=[],[]
f=open('address.txt','r')
fout1=open('col1.txt','w')
fout2=open('col2.txt','w')
i=0
for line in f:
	i+=1
	line=line.expandtabs(1)
	data=line.split(' ')
	x.append(data[0]+'\n')
	y.append(data[1])

fout1.writelines(x)
fout2.writelines(y)
f.close()
fout1.close()
fout2.close()
