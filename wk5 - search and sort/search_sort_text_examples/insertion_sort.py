# insertion sort

def insertion_sort(alist):
    passes = 0
    for index in range(1, len(alist)):
        currentvalue = alist[index]
        position = index

        while position > 0 and alist[position - 1] > currentvalue:
            alist[position] = alist[position - 1]
            position = position - 1
            passes += 1

        alist[position] = currentvalue

    print('number of passes: ', passes)

l = [25, 1, 5, 65, 30, 100, 10]
print(l)
print('---')
insertion_sort(l)
print('---')
print(l)
