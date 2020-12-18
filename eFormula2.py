factorials=1
x=0
count=1
result=1
while True:
    x+=1
    factorials=factorials*x
    result=result+1/factorials
    if x==100:
        print(result)
        exit()