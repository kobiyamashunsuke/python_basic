
f=open('col2.txt')
data = f.read()

# counting
words = {}
i=0
for word in data.split():
    i+=1
    words[word] = words.get(word, 0) + 1

# sort by count
d = [(v,k) for k,v in words.items()]
d.sort()
d.reverse()
count1=0
for count, word in d[:i]:
    count1+=1
    print count1,count, word

