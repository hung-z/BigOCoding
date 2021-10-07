import sys
sys.setrecursionlimit(1000000)


MAX = 10005
V = None
E = None

term = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

dr = [0, 0, 1, -1, 1, 1, -1, -1]
dc = [1, -1, 0, 0, 1, -1, 1, -1]


def check_valid(x, y):
    if x>=0 and x<H and y>=0 and y<W:
        return True
    return False

def DFSRecursion(s):
    count = 0 
    for i in range(len(dr)):
        v = [s[0] + dr[i], s[1]+dc[i]]
        if check_valid(v[0], v[1]) and ord(matrix[v[0]][v[1]])==ord(matrix[s[0]][s[1]])+1 and visited[v[0]][v[1]]==0:
            DFSRecursion(v)
            count = max(count, visited[v[0]][v[1]])
    visited[s[0]][s[1]] = count + 1
    return visited[s[0]][s[1]]

results = []
while(1):
    max_res = 0
    H, W = map(int, input().split())
    if H==0 and W==0:
        break
    matrix =[[] for i in range(H)]
    for i in range(H):
        matrix[i] = input()
    visited = [[0 for i in range(W)] for j in range(H)]
    for i in range(H):
        for j in range(W):
            if matrix[i][j] == 'A':
                max_res = max(max_res, DFSRecursion([i, j]))
    results.append(max_res)
for i, result in enumerate(results):
    print("case " + str(i+1) + ": " + str(result))
