a=set()
print(f'{a=} {type(a)=}')
a={}
print(f'{a=} {type(a)=}')
a={3,}
print(f'{a=} {type(a)=}')
a.add(5)
print(f'{a=} {type(a)=}')
a.remove(5)
print(f'{a=} {type(a)=}')
a.clear()
print(f'{a=} {type(a)=}')
a.add(5)
print(f'{a=} {type(a)=}')
del a
print(f'{a=} {type(a)=}')
