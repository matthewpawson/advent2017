arr = []
i = 0
count = 0
with open('day5in.txt') as inp:
    content = inp.readlines()
    for item in content:
        arr.extend(item.split())
for i in range(0, len(arr)):
    arr[i] = int(arr[i])
i = 0
while i < len(arr):
    temp = arr[i]
    if arr[i] < 3:      # only used in part B
        arr[i] += 1     # for part A, only use this line
    else:               # only used in part B
        arr[i] -= 1     # only used in part B
    i += temp
    count += 1
print(count)
