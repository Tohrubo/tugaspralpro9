nlist = [5, 2, 7, 1, 73, 12, 4, 134, 74, 12, 78, 21, 83]
nlist.sort()

count = 1
for i in range(3):
    print(f"Nilai terbaik ke-{count}: {nlist[-1-i]}")
    count += 1