def sequential_search(alist, item):

    iter = 0  # mine to count
    pos = 0
    found = False
    
    while pos < len(alist) and not found:
        iter+=1
        if alist[pos] == item:
            found = True
        else:
            pos = pos+1

    return found, iter

if __name__ == '__main__':
    l = [54, 26, 93, 17, 77, 31, 44, 55, 20, 65]
    item = 20
    print('list: ', l)
    print('item: ', item)
    print('item in list: ', sequential_search(l, item))


