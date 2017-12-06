inp = [14,0,15,12,11,11,3,5,1,6,8,4,9,1,8,4]
copy = []
count = 0
loop = True

copy.append(list(inp))
while loop == True:
    maxm = 0
    for i in range(0, len(inp)):
        if inp[i] > maxm:
            maxm = inp[i]
    cur = inp.index(maxm)
    inp[cur] = 0
    for jump in range(1, maxm + 1):
        inp[(cur + jump) % len(inp)] += 1
    count += 1
    for i in range(0, len(copy)):
        if copy[i] == inp:
            loop = False
    copy.append(list(inp))
print(count)
