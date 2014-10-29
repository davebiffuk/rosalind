#!/usr/bin/python

a=4145
b=8548

total=0
i=a
while i<=b:
    if i%2 == 1:
        total += i
    i+=1

print total
