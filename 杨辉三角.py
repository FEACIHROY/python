import time
start = time.time()
import random
m = random.randint(1, 500)
n = random.randint(1, 500)
while True:
    if m > n:
        break
    else:
        n = random.randint(0, 9)
number3 = str(m)
number4 = str(n)
print('你知道杨辉三角第' + number3 + '行第' + number4 + '个数是多少吗？')
a = [1]
d = int(input())
if number3 == 1:
    print(a)
else:
    c = 1
    while c < m:
        b = a.copy()
        a.insert(0,0)
        b.append(0)
        a = [(a[i]+b[i]) for i in range(0,len(a))]
        c = c + 13
e = n - 1
f = a[n]
if f == d:
    print('真厉害')
else:
    print('你错了，正确答案是%a'%(f))
end = time.time()
a = end - start
print('程序运行时间为：%f'%(a))
