length = 368078
horDisp = [0,1]
verDisp = [0,0,1]
temp = 0

count = 2
start = 1
cont = True

while cont == True:
    for i in range(0, count - 1):
        horDisp.extend([start])
    count += 1
    temp = (start * -1)
    while start > temp:
        start -= 1
        horDisp.extend([start])
        if start == temp:
            break
    start = temp
    for i in range(0, count - 1):
        horDisp.extend([start])
    count += 1
    temp = (start * -1) + 1
    while start < temp:
        start += 1
        horDisp.extend([start])
    start = temp
    if len(horDisp) > length:
        cont = False

cont = True
count = 3
start = 1

while cont == True:
    for i in range(0, count - 1):
        verDisp.extend([start])
    count += 1
    temp = (start * -1)
    while start > temp:
        start -= 1
        verDisp.extend([start])
        if start == temp:
            break
    start = temp
    for i in range(0, count - 1):
        verDisp.extend([start])
    count += 1
    temp = (start * -1) + 1
    while start < temp:
        start += 1
        verDisp.extend([start])
    start = temp
    if len(verDisp) > length:
        cont = False

print(abs(verDisp[length - 1]) + abs(horDisp[length - 1]))
    
# splits coordinates into relative displacement from the origin in both
# horizontal and vertical - each of these make a pattern of increasing
# repeats of a displacement, then counting down to the negative
# version of it. can and should be turned to classes at some point
