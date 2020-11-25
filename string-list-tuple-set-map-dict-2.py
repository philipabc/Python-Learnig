print("\n------- string ----------\n")
str0 = ''                   # create ---> C
str1 = " I am learning Python! "
str2 = "Python is awsome!"
print(str1+str2)
print(2*str1)
print(str2*2)

print(str1[4])      # read ---- R
print(str1[4:-1:2])
print(str1[4:-1:1])
print(str1[4:-1])
print(str1[0:-1])
print(str1[0:])
print(str1[:-1])

print(f'{str1=}')
# del str1[1]           #delete --> D  but the string is uchangeable
print(f'{str1=}')

# str1[1]="w"  # uchangeable ----> U

print("\n------- tuple ----------\n")
str0 = ()
str9 = (1,)
str1 = tuple(" I am learning Python! ")
str2 = tuple("Python is awsome!")
print(str1+str2)
print(2*str1)
print(str2*2)

print(str1[4])
print(str1[4:-1:2])
print(str1[4:-1:1])
print(str1[4:-1])
print(str1[0:-1])
print(str1[0:])
print(str1[:-1])

print(f'{str1=}')
# del str1[1]           #delete --> D  but the string is uchangeable
print(f'{str1=}')

# str1[1]="w"  # uchangeable

print("\n------- list ----------\n")
str0 = []
str1 = list(" I am learning Python! ")
str2 = list("Python is awsome!")
print(str1+str2)
print(2*str1)
print(str2*2)

print(str1[4])
print(str1[4:-1:2])
print(str1[4:-1:1])
print(str1[4:-1])
print(str1[0:-1])
print(str1[0:])
print(str1[:-1])
print(f'{str1=}')
str1[1] = "w"  # can be change --->U
print(f'{str1=}')
del str1[1]    #delete --> D
print(f'{str1=}')

print("\n------- set ----------\n")
str0 = set()
str00 = {1, 2}
str1 = set(" I am learning Python! ")
str2 = set("Python is awsome!")
print(str1)
print(str2)
str1.add(100)
print(str1)
str1.remove(100)
print(str1)
print(f'{str1 - str2=}')
print(f'{str1 | str2=}')
print(f'{str1 & str2=}')
print(f'{str1 ^ str2=}')

print("\n------- dictionary ----------\n")
str0={}
str1=dict([('apple',2),('pearl', 3),('orange',15)])
str2=dict(apple=2,pearl=3,orange=15)
print(f'{str1=}')
print(f'{str2=}')
str1['apple'] = 9  # can be change -->U
print(f'{str1["apple"]=}') 
print(f'{str1=}')
del str1['apple']  #delete --> D
print(f'{str1=}')

print(ord('中'))
print(ord('a'))
print(chr(ord('中')))
print(chr(ord('a')))
