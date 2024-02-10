# selection sort

def selectionSort(alist):
    passes = 0
    for fillslot in range(len(alist) - 1, 0, -1):
        print('fill slot: ', fillslot)
        pos_of_max = 0

        for i in range(1, fillslot + 1):
            if alist[i] > alist[pos_of_max]:
                pos_of_max = i
            passes += 1

        alist[fillslot], alist[pos_of_max] = alist[pos_of_max], alist[fillslot]

        print(alist)
    print('number of passes: ', passes)


l = [25, 1, 5, 65, 30, 100, 10]
print(l)
print('---')
selectionSort(l)
print('---')
print(l)
