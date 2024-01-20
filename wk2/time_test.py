import time
def sumOfN2(n):
   start = time.time()

   theSum = 0
   for i in range(1,n+1):
      theSum = theSum + i

   end = time.time()

   return theSum,end-start

for i in range(5):
    print("Sum is %d required %10.7f seconds"%sumOfN2(10000000))


def test1(n):
   print('test1--loop')
   l = []
   for i in range(n):
      l = l + [i]
   return l
