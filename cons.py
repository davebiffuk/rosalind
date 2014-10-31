from collections import defaultdict
d=defaultdict(str)

f=open('rosalind_cons.txt', 'r')
while True:
    l=f.readline().strip()
    if not l: break
    if l[0] == '>':
        label=l[1:]
        continue
    d[label] += l
    length=len(d[label])

print d

base={}
base['A']=[0] * length
base['C']=[0] * length
base['G']=[0] * length
base['T']=[0] * length

cons=[''] * length

for i in range(0,length):
    for k in d.keys():
        #print k, d[k], d[k][i]
        base[d[k][i]][i] += 1
    max=0
    for k in d.keys():
        if base[d[k][i]][i] > max:
            cons[i] = d[k][i]
            max = base[d[k][i]][i]

print "".join(cons)

for i in base.keys():
    print i + ':', ' '.join(map(str,base[i]))
