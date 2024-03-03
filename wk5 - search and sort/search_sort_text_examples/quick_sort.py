def quick_sort(alist):
   quick_sort_helper(alist, 0, len(alist) - 1)

def quick_sort_helper(alist, first, last):
   if first<last:
       splitpoint = partition(alist,first,last)
       quick_sort_helper(alist, first, splitpoint - 1)
       print('left: ', alist)
       quick_sort_helper(alist, splitpoint + 1, last)
       print('right: ', alist)


def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and \
               alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and \
               rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]

   alist[first], alist[rightmark] = alist[rightmark], alist[first]

   return rightmark


l = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print(l)
print('---')
quick_sort(l)
print('---')
print(l)