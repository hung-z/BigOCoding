
class Node:
    def __init__(self):
        self.countWord = 0
        self.child = dict()

def addWord(root, s, weight):
    temp = root
    for ch in s:
        if ch not in temp.child:
            temp.child[ch] = Node()
        temp.countWord = max(temp.countWord, weight)
        temp = temp.child[ch]

def findWord(root, s):
    temp = root
    for ch in s:
        if ch not in temp.child:
            return False
        temp = temp.child[ch]
    return temp.countWord

def isWord(Node):
    return node.countWord != 0

def isEmpty(Node):
    return len(node.child) == 0

def removeWord(root, s, level, len):
    if root == None:
        return False
    if level == len:
        if root.countWord > 0:
            root.countWord -=1
            return True
        return False
    ch = s[level]
    if ch not in root.child:
        return False
    flag = removeWord(root.child[ch], s, level+1, len)
    if flag == True and isWord(root.child[ch]) == False and isEmpty(root.child[ch]) == True:
        del root.child[ch]
    return flag

def printWord(root, s):
    if isWord(root):
        return s
    for ch in root.child:
        printWord(root.child[ch], s+ch)

n, q = map(int, input().split())
root = Node()
for i in range(n):
    string, weight = input().split()
    weight = int(weight)
    addWord(root, string, weight)
results = []
for i in range(q):
    string = input()
    weight = findWord(root, string)
    if(weight<=0):
        results.append(-1)
    else:
        results.append(weight)
for result in results:
    print(result)




