import math
import copy

n=5

print math.factorial(n) * 2 ** n

def permsigns(l):
    for i in range(0, 2**len(l)):
        a = copy.copy(l) # ugh
        # make negative the members in a which match the binary
        # representation of i
        for j in range(0, len(l)):
            if 2**j & i:
                a[j] = '-' + a[j]
        print ' '.join(a)

def permutations(head, tail=''):
    if len(head) == 0:
        permsigns(list(tail))
    else:
        for i in range(len(head)):
            permutations(head[0:i] + head[i+1:], tail+head[i])

s=""
while n>0:
    s = str(n) + s
    n -=1

permutations(s)
