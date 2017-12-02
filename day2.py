total = 0
with open('day2in.txt') as inp:
    content = inp.readlines()
    for lines in content:
        splitLine = lines.split()
        for num in splitLine:
            num = int(num)
            if num > maxN:
                maxN = num
            if (num < minN) or (minN == 0):
                minN = num
        total += (int(maxN) - int(minN))
print(total)
