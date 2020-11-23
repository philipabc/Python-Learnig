

hi=input("Please type which do you want to pick mean,median or mode? ") #"median" # 
if hi=="median" or hi=="Median":
    median=[]
    number2=(int(input("Please type how many numbers your going to type in: ")))
    for e in range(0,number2,1):
        median.append(int(input("now please type the numbers you want to find out the median of: ")))
    length2=len(median)
for t in range(number2):
    for g in range(t+1,number2):
        if median[t]>median[g]:
            tmp=median[t]
            median[t]=median[g]
            median[g]=tmp
            print(median)
            
if length2%2==1:
    almstdne=length2//2
    print("The median of that str is",median[almstdne])
elif length2%2==0:
    almstdne2=length2//2-1
    almstdne3=length2//2
    total=(median[almstdne2]+median[almstdne3])/2
    print("the median of that str is",total)
    
    