import time
from datetime import datetime

start=time.time()
time.sleep(4)
stop=time.time()

diff=stop-start
print(f'{start=}')
print(f'{((stop-start)//60)=} minutes')
print(stop)
print(diff)
print(time.time())

print(a:=datetime.today())
print(b:=datetime.now())
print(a.year)
print(b.year)
print(b.hour)
print(b.day)
print(b.second)
print(b.weekday())


a=time.perf_counter()
time.sleep(1)
b=time.perf_counter()
print(a,b,a-b)

c=time.ctime()
print(c)
print(d:=c.split(' '))
print([d[i] for i in range(len(d))])