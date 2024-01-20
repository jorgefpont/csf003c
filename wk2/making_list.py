import time
import timeit

def test1(n):
    #print('test1--loop')
    l=[]
    for i in range(n):
        l = l + [i]
    return l

def test2(n):
    #print('test2--append')
    l=[]
    for i in range(n):
        l.append(i)
    return l

def test3(n):
    #print('test3--list comprehension')
    l = [i for i in range(n)]
    return l

def test4(n):
    #print('test4--list range')
    l = list(range(n))
    return l

n = 10000

t1 = timeit.Timer("test1(n)", "from __main__ import test1, n")
print("concat ", t1.timeit(number=1000), "milliseconds")

t2 = timeit.Timer("test2(n)", "from __main__ import test2, n")
print("append ", t2.timeit(number=1000), "milliseconds")

t3 = timeit.Timer("test3(n)", "from __main__ import test3, n")
print("comprehension ", t3.timeit(number=1000), "milliseconds")

t4 = timeit.Timer("test4(n)", "from __main__ import test4, n")
print("list range ", t4.timeit(number=1000), "milliseconds")