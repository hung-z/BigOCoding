import collections
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

def BFS(s):
    q = Queue()
    visited[s[0]][s[1]] = True
    q.put(s)
    count = 1
    while not q.empty():
        u = q.get()
        for i in range(4):
            x = X[i]
            y = Y[i]
            if(not validate(u[0]+x, u[1]+y)):
                continue
            v = [u[0]+x, u[1]+y]
            if (not visited[v[0]][v[1]]) and (matrix[v[0]][v[1]]=='1'):
                visited[v[0]][v[1]] = True
                q.put(v)
                count += 1
    return count
results = []
while(1):
    N, M = map(int, input().split())
    if(N==0 and M==0):
        break
    matrix = []
    count_dict = {}
    for i in range(N):
        matrix.append(list(input().split()))
    visited = [[False for i in range(M)] for j in range(N)]

    for i in range(N):
        for j in range(M):
            if matrix[i][j] == '1' and (not visited[i][j]):
                source = [i, j]
                num_1s = BFS(source)
                if not (num_1s in count_dict):
                    count_dict[num_1s] = 0
                count_dict[num_1s] += 1
    count_dict = collections.OrderedDict(sorted(count_dict.items()))
    results.append(count_dict)
for result in results:
    print(sum(result.values()))
    for key in result:
        print(str(key)+' '+str(result[key]))


