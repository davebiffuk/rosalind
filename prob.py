# Given: A DNA string s of length at most 100 bp and an array A
# containing at most 20 numbers between 0 and 1.

# Return: An array B having the same length as A in which B[k]
# represents the common logarithm of the probability that a random
# string constructed with the GC-content found in A[k] will match s
# exactly.

import math

f=open('rosalind_prob.txt', 'r')
s=f.readline().strip()
aa=f.readline().strip()

b=[]

for a in map(float,aa.split()):
    # calculate probability that s would match random string with GC
    # content = a
    cumprob=0
    for i in s:
        if i == 'G' or i == 'C':
            cumprob += math.log10(a/2)
        else:
            cumprob += math.log10((1-a)/2)
    b.append(cumprob)

#print ' '.join(map(str,b))
print ' '.join(map(str,[round(i,3) for i in b]))
