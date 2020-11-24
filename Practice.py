from randomlist import randomlist
print(randomlist(10))

mode=[1,2,3,4,4,1,1,3,4,2,5,6]

# sort the list
length=len(mode)
for b in range(length):
    for k in range(b+1,length):
        if mode[b]>mode[k]:
            tmp=mode[b]
            mode[b]=mode[k]
            mode[k]=tmp
print(mode)

# find the number of occurence
current=0
dic={}
count=1
for k in range(1,length):
    if mode[k]==mode[current]:  
        count+=1
    else:
        dic[mode[current]]=count    
        if k==length-1:
            dic[mode[k]]=1
        else:
            count=1
            mode[current]=mode[k]
print(dic)

# get the mode of list---2 steps
valuesList=list(dic.values())
print(valuesList)
max=valuesList[0]
# step 1: get the max of values
for v in valuesList:
    if max<v:
        max=v
print(max)
# step 2: get the keys of max
modes=[]
for (k,v) in dic.items():
    if v==max:
        modes.append(k)
print(modes)
        


