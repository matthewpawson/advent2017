args = []
regs = {}
maxm = 0
with open('day8in.txt') as inp:
    content = inp.readlines()
    for lines in content:
        splitLine = lines.split()
        args.append(splitLine[:3])
        args[len(args) - 1].append(lines.split('if')[1].strip())
        
for i in range(0, len(args)):
    if not args[i][0] in regs:  # poplate dictionary with all needed registers
        regs[args[i][0]] = 0    # so no missing key error is found
print(regs)
for i in range(0, len(args)):
    if eval(args[i][3], regs):  # if the comparison is correct
        regs[args[i][0]] += ((1 if args[i][1] == 'inc' else -1) * int(args[i][2]))
        if regs[args[i][0]] > maxm:
            maxm = regs[args[i][0]]

print(maxm)      # max(regs.values()) for part 1

# weird error is present - error dcumentation is appened to dictionary
# for some unknown reason, to be fixed after AOC
