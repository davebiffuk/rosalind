f=open('rosalind_subs.txt', 'r')

s=f.readline().strip()
t=f.readline().strip()

w=[]

for i in range(0,len(s)):
    if s[i:i+len(t)] == t:
        w.append(i+1)

print " ".join(map(str,w))
