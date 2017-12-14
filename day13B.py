col = []
depth = []
with open('day13in.txt') as inp:
    content = [line.strip() for line in inp]
    col.extend([lines.split(': ')[0] for lines in content])
    depth.extend([lines.split(': ')[1] for lines in content])
col = list(map(int, col))        # turn strings to ingegers
depth = list(map(int, depth))    # turn strings to integers
delay = 0
caught = True
while caught == True:
    count = delay
    nextCol = 0
    caught = False
    for i in range(0, int(col[len(col) - 1]) + 1):
        if i in col:
            if count % ((2 * depth[nextCol]) - 2) == 0:
                caught = True
                if caught:
                    break
            nextCol += 1
        count += 1
    if caught == False:
        print(delay)
    else:
        delay += 1
