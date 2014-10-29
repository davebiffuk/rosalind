#!/usr/bin/python

n=36
k=2

q=0
r=1

i=1
while i<n:
    p = r
    r += q*k
    q = p
    i += 1

print r

