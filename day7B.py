root = []
node = []
links = {}
tots = {}
def init():
    with open('day7in.txt') as inp:
        content = inp.readlines()
        for line in content:
            if "->" in line:
                root.append(line.split())
        for line in content:
            node.append(line.split())

    for i in range(0, len(node)):
        links[node[i][0]] = node[i][1].strip('()')
    for i in range(0, len(root)):
        temp = [root[i][1].strip('()')]
        for j in range(3, len(root[i])):
            temp.append(root[i][j].strip(','))
        links[root[i][0]] = temp
    calcBal()
    
def calcBal():                          
    for name in links:
        if type(links[name]) == list:
            arr = links[name]
            total = getVal(arr[1:])
            tots[name] = int(arr[0]) + total
        else:
            tots[name] = int(links[name])
    compWeights()

def compWeights():
    for i in range(0, len(root)):
        arr = [[],[]]
        for element in root[i][3:]:
            arr[0].append(tots[element.strip(',')])
            arr[1].append(element)
        if len(set(arr[0])) != 1:
            print(arr)          # ans is smallest of outputs due to stacking
            
def getVal(arr):
    total = 0
    for name in arr:
        if type(links[name]) == list:
            total += int(links[name][0])
            total += getVal(links[name][1:])
        else:
            total += int(links[name])
    return total

init()
