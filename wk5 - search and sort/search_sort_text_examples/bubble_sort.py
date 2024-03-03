# bubble sort
# each pass moves the remaining largest number to the back


def bubbleSort(alist):
    passes = 0
    for passnum in range(len(alist)-1, 0, -1):
        print('pass number: ', passnum)
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]

            print(i, alist)
            passes += 1
    print('number of passes: ', passes)

l = [25, 1, 5, 65, 30, 100, 10]
print(l)
print('---')
bubbleSort(l)
print('---')
print(l)
