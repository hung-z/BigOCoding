MAX = 100005
V = None
E = None
visited = [False for i in range(MAX)]
graph = [[] for i in range(MAX)]

def DFS(src):
    s = []
    visited[src] = True
    s.append(src)
    while len(s) > 0:
        u = s.pop()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                s.append(v)

T = int(input())
results = []
for i in range(T):
    visited = [False for i in range(MAX)]
    graph = [[] for i in range(MAX)]
    V = int(input())
    E = int(input())
    if(E==0):
        results.append(V)
        continue
    for j in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    count = 0
    for j in range(V):
        if not visited[j]:
            DFS(j)
            count += 1
    results.append(count)
for result in results:
    print(result)
