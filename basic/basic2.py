#!/user/bin/env python

x,y=[],[]
f=open('address.txt','r')
i=0
for line in f:
	i+=1
	line=line.expandtabs(1)
	line = line.replace('\n','')
        print line

f.close()
