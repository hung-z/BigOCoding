
class Node:
    def __init__(self):
        self.countWord = 0
        self.child = dict()

def addWord(root, s):
    temp = root
    for ch in s:
        if ch not in temp.child:
            temp.child[ch] = Node()
        temp = temp.child[ch]
    temp.countWord += 1

def findWord(root, s):
    temp = root
    for ch in s:
        if ch not in temp.child:
            return False
        temp = temp.child[ch]
    return temp.countWord > 0

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




