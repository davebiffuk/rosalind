import math

n=6

print math.factorial(n)

def permutations(head, tail=''):
    if len(head) == 0:
        print ' '.join(list(tail))
    else:
        for i in range(len(head)):
            permutations(head[0:i] + head[i+1:], tail+head[i])

s=""
while n>0:
    s = str(n) + s
    n -=1

permutations(s)
