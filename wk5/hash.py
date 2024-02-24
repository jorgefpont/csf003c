
l_size = 11
l = [54, 26, 93, 17, 77, 31]

positions = []
for i in l:
  positions.append(i%l_size)

print('positions: ', positions)
print('list: ', l)

hashed = [None]*11
print(hashed)

j=0
for i in positions:
    hashed[i] = l[j]
    j+=1

print(hashed)
