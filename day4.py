ans = 0
temp = ''
with open('day4in.txt') as inp:
    content = inp.readlines()
    for lines in content:
        splitLine = lines.split()
        total = 0
        for anagram in splitLine:   # module is required for part B of the
            l = list(anagram)       # task: it sorts every word prior to checking
            l.sort()                # in order for comparison
            splitLine[splitLine.index(anagram)] = ''.join(l)
        for word in splitLine:
            for check in splitLine:
                if check == word:
                    total += 1
        if total <= len(splitLine):
            ans += 1
print(ans)
