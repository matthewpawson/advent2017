total = 0
with open('day2in.txt') as inp:
    content = inp.readlines()
    for lines in content:
        splitLine = lines.split()
        for num in splitLine:
            num = int(num)
            for mod in splitLine:
                mod = int(mod)
                if num % mod == 0 and num != mod:
                    total += int(num / mod)
print(total)
