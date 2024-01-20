from timeit import Timer

def build_list(n):
    # fastest way to build a list
    return list(range(n))

def build_dict(n):
    # fastest way to build a dict
    return {i : str(i) for i in range(n)}

def inx(x,n):
    str(0) in x
    str(n//2) in x
    str(n-1) in x
    "a" in x

timelist = Timer(
    "inx(x,n)",
    "from __main__ import n, build_list, inx; x=build_list(n)")

timedict = Timer(
    "inx(x,n)",
    "from __main__ import n, build_dict, inx; x=build_dict(n)")

print("N", "\t", "List", "\t", "Dict")
for size in range(1000, 100000+1, 5000):
    n = size
    list_secs = timelist.repeat(5,5)
    dict_secs = timedict.repeat(5,5)
    print(n, "\t", min(list_secs), "\t", min(dict_secs))
