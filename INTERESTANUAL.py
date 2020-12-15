hi=float(input("Hello,how much are you going to give? "))
print("Okay!")
print("i will give you 1 plus in a year")
dollars=01
day=1/356
week=7*day
month=4*week
y=356*day
# print(dollars,day,week,month,y)
hi2=(input("Welcome back!You want your money back?ok then can you type if tis been weeks or days etc?(week,month or y as in year)"))
hi3=float(input("Thank you!ok ca you type how many its been?"))
print("Thank you!Ok lemme see how much money you will get")
if hi2=="week":
    print("how much you will get is ",week*hi3)
elif hi2=="day":
    print("how much you will get is ",day*hi3)
elif hi2=="month":
    print("how much you will get is ",month*hi3)
elif hi2=="year" or hi2=="Year" or hi2=="y" or hi2=="Y":
    print("how much you will get is ",y*hi3)
else:
    print("Sorry! something went wrong :(")
