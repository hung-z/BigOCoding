from queue import Queue
MAX = 255
V = None
E = None
visited = [False for i in range(MAX)]
graph = [[] for i in range(MAX)]

X = [0,0,-1,1]
Y = [-1,1,0,0]
def validate(x, y):
    if(x>=0 and x<N and y>=0 and y<M):
        return True
    return False

def margin(x, y):
    if x==0 or y==0 or x==N-1 or y==M-1:
        return True
    return False

def BFS(s):
    q = Queue()
    visited[s[0]][s[1]] = True
    q.put(s)
    sheeps = 0
    wolves = 0
    mark = matrix[s[0]][s[1]]
    if(mark == 'k'):
        sheeps += 1
    elif(mark == 'v'):
        wolves += 1
    rounded = True
    while not q.empty():
        u = q.get()
        for i in range(4):
            x = X[i]
            y = Y[i]
            if(not validate(u[0]+x, u[1]+y)):
                continue
            v = [u[0]+x, u[1]+y]
            if not visited[v[0]][v[1]]:
                mark = matrix[v[0]][v[1]]
                if mark == 'k':
                    sheeps += 1
                    visited[v[0]][v[1]] = True
                    q.put(v)
                elif mark == 'v':
                    wolves += 1
                    visited[v[0]][v[1]] = True
                    q.put(v)
                elif mark == '.':
                    if(margin(v[0], v[1])):
                        rounded = False
                    visited[v[0]][v[1]] = True
                    q.put(v)
    # print(sheeps, wolves)
    if not rounded:
        return sheeps, wolves
    if(sheeps>wolves):
        return sheeps, 0
    else:
        return 0, wolves    


N, M = map(int, input().split())
matrix = []
for i in range(N):
    matrix.append(input())
visited = [[False for i in range(M)] for j in range(N)]

num_sheep = 0
num_wolf = 0
for i in range(N):
    for j in range(M):
        if (not visited[i][j]) and (matrix[i][j]!='#'):
            source = [i, j]
            k, v = BFS(source)
            num_sheep += k
            num_wolf += v

print(str(num_sheep)+' '+str(num_wolf))

