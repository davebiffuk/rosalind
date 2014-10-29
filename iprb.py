k=2.0 # hom dom
m=1.0 # het
n=2.0 # hom rec

t=k+m+n

pk=k/t
pm=m/t
pn=n/t

# probability of recessive
#    both hom rec       both het rec               het rec + hom rec
pr = pn*((n-1)/(t-1)) + pm*0.5*((m-1)/(t-1))*0.5 + 2*pn*0.5*((m)/(t-1))

# probability of dominant allele
print 1-pr
