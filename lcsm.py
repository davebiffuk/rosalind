from collections import defaultdict
d=defaultdict(str)

count=0
f=open('rosalind_lcsm.txt', 'r')
while True:
    l=f.readline().strip()
    if not l: break
    if l[0] == '>':
        label=l[1:]
        count+=1
        continue
    d[label] += l
    length=len(d[label])

lcsm=""

string=d[label]

for i in xrange(len(string)):
    for j in range(i,len(string)):
        if (j+1-i) < len(lcsm):
            continue
        subs=string[i:j+1]
        c = 0
        for k2 in d.keys():
            if k2 == label:
                continue
            if subs in d[k2]:
                c += 1
        if c == count-1:
            if len(subs) > len(lcsm):
                lcsm = subs
                #print lcsm

print lcsm

