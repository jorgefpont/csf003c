def choosing(n, k):
    if k == 0 or k == n:
        return 1
    elif n < k:
        return 0
    else:
        return choosing(n-1, k-1) + choosing(n-1, k)

print(choosing(2,1))
print(choosing(1,2))
print(choosing(2,6))