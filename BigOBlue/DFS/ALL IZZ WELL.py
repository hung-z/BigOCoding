
MAX = 10005
V = None
E = None

term = "ALLIZZWELL"

dr = [0, 0, 1, -1, 1, 1, -1, -1]
dc = [1, -1, 0, 0, 1, -1, 1, -1]


def check_valid(x, y):
    if x>=0 and x<R and y>=0 and y<C:
        return True
    return False

def DFSRecursion(s, count):
    global found
    if count == len(term):
        found = True
        return True
    for i in range(len(dr)):
        v = [s[0] + dr[i], s[1]+dc[i]]
        if check_valid(v[0], v[1]) and matrix[v[0]][v[1]]==term[count] and not visited[v[0]][v[1]]:
            visited[v[0]][v[1]] = True
            DFSRecursion(v, count+1)
            visited[v[0]][v[1]] = False

t = int(input())
results = []
for i in range(t):
    R, C = map(int, input().split())
    visited = [[False for i in range(C)] for i in range(R)]
    matrix = [[] for i in range(R)]
    for j in range(R):
        matrix[j] = input()
    line = input()
    found = False
    for j in range(R):
        for k in range(C):
            if matrix[j][k]=='A':
                src = [j,k]
                DFSRecursion(src, 1)
    if found:
        results.append('YES')
    else:
        results.append('NO')

for result in results:
    print(result)
