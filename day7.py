roots = []

with open('day7in.txt') as inp:
    content = inp.readlines()
    for line in content:
        if "->" in line:
            roots.append(line.split())

for i in range(0, len(roots)):
    item = roots[i][0]
    found = False
    for j in range(0, len(roots)):
        for k in range(3, len(roots[j])):
            roots[j][k] = roots[j][k].strip(',')
            if item == roots[j][k]:
                found = True
    if not found:
        print(item)

