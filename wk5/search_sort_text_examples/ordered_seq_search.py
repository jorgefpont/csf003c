def ordered_seq_search(alist, item):
    iter = 0  # mine to count
    pos = 0
    found = False
    stop = False
    while pos < len(alist) and not found and not stop:
        iter+=1
        if alist[pos] == item:
            found = True
        else:
            if alist[pos] > item:
                stop = True
            else:
                pos = pos+1

    return found, iter

if __name__ == '__main__':
    l = [1, 2, 5, 10, 20, 25, 30, 35]
    item = 20
    print('list: ', l)
    print('item: ', item)
    print('item in list: ', ordered_seq_search(l, item))
