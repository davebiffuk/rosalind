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

# pick the last one to work from
string=d[label]

# len(string) - n  is the length of substring to consider
for n in range(0, len(string)):
    for k in range(0, n+1):
        sub=string[k:k+len(string)-n]
        #print "considering substring length ", len(string)-n, " from pos", k, sub
        c = 0
        for k2 in d.keys():
            if k2 == label:
                continue
            if sub not in d[k2]:
                break # no point checking any further
            c += 1
        if c == count-1:
            print sub
            break
    if c == count-1:
        break
