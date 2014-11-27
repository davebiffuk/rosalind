f=open('rosalind_lgis.txt', 'r')
f.readline()
perm=map(int,f.readline().strip().split())
n=len(perm)

# algorithm idea from
# https://github.com/sefakilic/rosalind/blob/master/rosalind_utils.py

def lgis(perm):
    # initialize to correct length with "None"; overwrite as we walk the list
    lttp=[None] * n # length of longest sequence to this point
    prev=[None] * n # index of previous number in longest sequence to this point

    for d in range(n):
        # initially consider each number as the end of a sequence of length 1
        lttp[d]=1
        prev[d]=-1
        # examine each previous perm[i] to see if a longer sequence
        # could be constructed by appending this number
        for i in range(d):
            if perm[i] < perm[d] and lttp[i]+1 > lttp[d]:
                # if so, record the new length to this point, and the
                # index of the previous number
                lttp[d] = lttp[i]+1
                prev[d] = i

    # what is the index of the number that ends the longest subsequence?
    i = lttp.index(max(lttp))
    # reconstruct the sequence by walking the pointer indices backwards
    seq=[]
    while i > -1:
        seq.append(perm[i])
        i = prev[i]
    seq.reverse()
    return seq

print ' '.join(map(str,lgis(perm)))
perm.reverse()
r=lgis(perm)
r.reverse()
print ' '.join(map(str,r))
