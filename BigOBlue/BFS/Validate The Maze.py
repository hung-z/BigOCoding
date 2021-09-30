from queue import Queue
X = [0,0,-1,1]
Y = [-1,1,0,0]
def validate(x, y):
    if(x>=0 and x<N and y>=0 and y<M):
        return True
    return False
def BFS_xy(s):
    for i in range(N):
        for j in range(M):
            visited[i].append(False)
    q = Queue()
    visited[s[0]][s[1]] = True
    q.put(s)
    while not q.empty():
        u = q.get()
        for i in range(4):
            x = X[i]
            y = Y[i]
            if(not validate(u[0]+x, u[1]+y)):
                continue
            v = [u[0]+x, u[1]+y]           
            if (not visited[v[0]][v[1]]) and maze[v[0]][v[1]]=='.':
                if(v[0]==0 or v[0]==N-1 or v[1]==0 or v[1]==M-1):
                    return 'valid'
                visited[v[0]][v[1]] = True
                q.put(v)
    return 'invalid'

Q = int(input())
results = []
for i in range(Q):
    N, M = map(int, input().split())
    maze = [[] for i in range(N)]
    visited = [[] for j in range(N)]
    for i in range(N):
        for j in range(M):
            visited[i].append(False)
    exit_count = 0
    for i in range(N):
        row = input()
        for j in range(M):
            maze[i].append(row[j])
            if(i==0 or i==N-1 or j==0 or j==M-1):
                if row[j] == '.':
                    exit_count+=1
                    source = [i, j]
    if(exit_count!=2):
        results.append("invalid")
    else:
        results.append(BFS_xy(source))

for result in results:
    print(result)
