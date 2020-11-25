print("\n------- string ----------\n")
str0 = ''
str1 = " I am learning Python! "
str2 = "Python is awsome!"
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

# str1[1]="w"

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

# str1[1]="w"

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

str1[1] = "w"

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


print(ord('中'))
print(ord('a'))
print(chr(ord('中')))
print(chr(ord('a')))
