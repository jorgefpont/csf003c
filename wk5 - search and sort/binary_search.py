#iterative
def binarySearch(alist, item):
   first = 0
   last = len(alist) -1
   found = False

   while first <= last and not found:
       midpoint = (first + last) // 2
       if alist[midpoint] == item:
           found = True
       else:
           if item < alist[midpoint]:
               last = midpoint - 1
           else:
               first = midpoint + 1

   return found

demolist = [0, 1, 2, 8, 11, 12, 15, 31, 33,]
print(binarySearch(demolist, 4))
print(binarySearch(demolist, 31))

'''
False
True
'''


#recursive
def binarySearch(alist, item):
   if len(alist) == 0:
      return False
   else:
      midpoint = len(alist)//2
      if alist[midpoint] == item:
          return True
      else:
          if item < alist[midpoint]:
              return binarySearch(alist[:midpoint],item)
          else:
              return binarySearch(alist[midpoint + 1:], item)

demolist = [0, 1, 2, 8, 11, 12, 15, 31, 33,]
print(binarySearch(demolist, 4))
print(binarySearch(demolist, 31))
'''
False
True
'''
