score = 0
inc = 1
i = 0
garb = False
garbage = 0
with open('day9in.txt') as file:
    inp = file.read().replace('\n','')
while i < len(inp):
    char = inp[i]
    if char == '!':
        i += 1
    elif garb == True:
        if char != '>':
            garbage += 1
    elif char == '{':
        score += inc
        inc += 1
    elif char == '}':
        inc -= 1
    elif char == '<':
        garb = True
    if char == '>':     # cant address garb in == True conditional.
        garb = False
    i += 1

print(score, garbage)   # score is part 1, garbage is part 2

