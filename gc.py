label=''
d={}
f=open('/home/dh3/Downloads/rosalind_gc.txt', 'r')

for line in f:
    line = line.strip()
    if line[0]=='>':
        if label != '':
            d[label] = content
        label=line[1:]
        content=''
        continue
    content += line
d[label] = content

print d

max = 0
for i in d.keys():
    gc = float(d[i].count('G') + d[i].count('C')) / len(d[i])
    print i, gc
    if gc > max:
        maxlabel = i
        max = gc

print maxlabel
print max*100
#print("%.6f" % max)
