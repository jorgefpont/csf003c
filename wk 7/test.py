l = ['html', 'body', 'h1', 'W3C Mission', 'ul', 'li', 'Web for All', 'li', 'li', 'Web on Everything', 'li', 'ul', 'ul', 'li', 'list2-1', 'li', 'li', 'list2-2', 'li', 'ul','body', 'html']



def parse_list(l):
    ll = []
    i = 0
    while i < len(l):
        if l[i] == 'ul':
            # position of the next (closing) 'ul'
            end_tag = l.index('ul', i+1)
            ll.append(l[i+1 : end_tag])
            i = end_tag + 1
        else:
            i += 1
    return ll


def remove_li(ll):
    for j in range(len(ll)):
        ll[j] = [x for x in ll[j] if x != 'li']

print(l)
ll = parse_list(l)
print(ll)
remove_li(ll)
print(ll)



