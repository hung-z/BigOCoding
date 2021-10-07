MAX = 10005
V = None
E = None
visited = [False for i in range(MAX)]
inPath = [False for i in range(MAX)]
path = [0 for i in range(MAX)]
graph = [[] for i in range(MAX)]

def DFS(src):
    s = []
    visited[src] = True
    s.append(src)
    inPath[src] = True
    while len(s) > 0:
        u = s.pop()
        for v in graph[u]:
            if (not visited[v]) and (not inPath[v]):
                visited[v] = True
                inPath[v] = True
                s.append(v)
            elif(visited[v] and inPath[v]):
                return True
    inPath[src] = False
    return False


T = int(input())
results = []
for i in range(T):
    inPath = [False for i in range(MAX)]
    visited = [False for i in range(MAX)]
    graph = [[] for i in range(MAX)]
    V, E = map(int, input().split())
    for j in range(E):
        u, v = map(int, input().split())
        u, v = u - 1, v - 1
        graph[u].append(v)
    have_loop = False
    for j in range(V):
        if not visited[j]:
            have_loop = DFS(j)
            if have_loop:
                results.append('YES')
                break
    if not have_loop:
        results.append('NO')
for result in results:
    print(result)

    
