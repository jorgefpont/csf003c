def binary_search(alist, item):
    iter = 0  # mine to count
    first = 0
    last = len(alist)-1
    found = False

    while first<=last and not found:
        iter+=1
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1

    return found, iter

if __name__ == '__main__':
    l = [54, 26, 93, 17, 77, 31, 44, 55, 20, 65]
    item = 20
    print('list: ', l)
    print('item: ', item)
    print('item in list: ', binary_search(l, item))
