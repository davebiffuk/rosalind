f=open('/home/dh3/Downloads/rosalind_hamm.txt', 'r')

a=f.readline().strip()
b=f.readline().strip()

count=0
for char in a:
    if char != b[0]:
        count += 1
    b=b[1:]

print count
