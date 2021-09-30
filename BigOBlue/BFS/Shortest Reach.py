from queue import Queue
MAX = 1005
def BFS(s):
    for i in range(N):
        visited[i] = False
        path[i] = -1
    q = Queue()
    visited[s] = True
    q.put(s)
    while not q.empty():
        u = q.get()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                q.put(v)
                path[v] = u
def cal_distance(s, f):
    b  = []
    if f == s:
        return 0
    if path[f] == -1:
        return -1
    while(True):
        b.append(f)
        f = path[f]
        if f == s:
            b.append(s)
            break
    return len(b) - 1


Q = int(input())
results_list = []
for i in range(Q):
    N, M = map(int, input().split())
    visited = [False for i in range(MAX)]
    path = [0 for i in range(MAX)]
    graph = [[] for i in range(MAX)]
    for i in range(M):
        u, v = map(int, input().split())
        u, v = u-1, v-1
        graph[u].append(v)
        graph[v].append(u)
    source = int(input())
    source = source - 1
    BFS(source)
    results = []
    for j in range(N):
        if j == source:
            continue
        distance = cal_distance(source, j)
        if(distance!=-1):
            distance*=6
        results.append(distance)
    results_list.append(results)
for results in results_list:
    for k in range(len(results)):
        if(k<len(results)-1):
            print(results[k], end=' ')
        else:
            print(results[k], end='\n')

