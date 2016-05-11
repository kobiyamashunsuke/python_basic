f=open('col1.txt')
data = f.read()

# counting
words = {}
for word in data.split():
    words[word] = words.get(word, 0) + 1

# sort by count
d = [(v,k) for k,v in words.items()]
d.sort()
d.reverse()
count1=0
for count, word in d[:100000]:
    count1+=1
    print count1,count, word

