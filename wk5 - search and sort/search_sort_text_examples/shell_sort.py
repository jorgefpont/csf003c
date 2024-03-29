"""
The shell sort, sometimes called the “diminishing increment sort,”
improves on the insertion sort by breaking the original list into a number of smaller sublists,
each of which is sorted using an insertion sort. The unique way that these sublists are chosen
is the key to the shell sort. Instead of breaking the list into sublists of contiguous items,
the shell sort uses an increment i, sometimes called the gap, to create a sublist by choosing
all items that are i items apart.
"""

def shell_sort(alist):
    # initial gap (large)
    #sublistcount = len(alist) // 2
    sublistcount = 2

    while sublistcount > 0:

        for startposition in range(sublistcount):
            gapInsertionSort(alist, startposition, sublistcount)

        print("After increments of size", sublistcount,
              "the list is", alist)
        sublistcount //= 2


def gapInsertionSort(alist, start, gap):
    print('call to gap insertion sort ftn (gap val): ', gap)

    for i in range(start + gap, len(alist), gap):

        currentvalue = alist[i]
        position = i

        while position >= gap and \
                alist[position - gap] > currentvalue:

            alist[position] = alist[position - gap]
            position = position - gap

        alist[position] = currentvalue


#l = [54, 26, 93, 17, 77, 31, 44, 55, 20]
l=[5, 16, 20, 12, 3, 8, 9, 17, 19, 7]

print(l)
print('---')
shell_sort(l)
print('---')
print(l)


