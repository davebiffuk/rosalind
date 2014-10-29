#!/usr/bin/python

f=open("Downloads/rosalind_ini5.txt", "r")

n=1

for line in f: 
    line = line.strip()
    if n%2 == 0:
        print line
    n+=1
