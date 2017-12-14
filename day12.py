dic = {}
count = 0
visited = []
nodes = ['0']
with open('day12in.txt') as inp:
    content = inp.readlines()
    for line in content:        
        arr = line.split(' <->')[1].split(',')
        arr = [item.strip() for item in arr]
        dic[line.split(' <->')[0]] = arr
while len(nodes) != 0:
    if nodes[0] not in visited:
        count += 1
        for node in dic[nodes[0]]:
            nodes.append(node)
        visited.append(nodes[0])
    nodes.pop(0)
print(count, visited)

