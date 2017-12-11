arr = []
x = 0
y = 0
z = 0
maxm = 0
with open('day11in.txt') as inp:
    content = inp.readlines()
    for line in content:
        arr.extend(line.strip().split(','))

for element in arr:    # using hex represetation in 2d plane
    if element == 'n':      # nw | n  |
        y += 1              # -------------
    elif element == 's':    # sw |    | ne
        y -= 1              # -------------       
    elif element == 'ne':   #    |  s | se
         x += 1
    elif element == 'se':
        y -= 1
        x += 1
    elif element == 'nw':
        y += 1
        x -= 1
    elif element == 'sw':
        x -= 1
    cur = (abs(x) + abs(y) + abs(x+y)) / 2
    if cur > maxm:
        maxm = cur
        
print(cur, maxm)   # cur for part 1, maxm for part 2
