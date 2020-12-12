from randomlist import randomlist
# print(randomlist(10))

mode=[1,2,3,4,4,1,1,3,4,2,4,4]

# sort the list
length=len(mode)
for b in range(length):
    for k in range(b+1,length):
        if mode[b]>mode[k]:
            tmp=mode[b]
            mode[b]=mode[k]
            mode[k]=tmp
print(mode)