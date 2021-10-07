MAX = 10005
V = None
E = None
visited = [False for i in range(MAX)]
path = [0 for i in range(MAX)]
graph = [[] for i in range(MAX)]

def DFSRecursion(s):
    visited[s] = True
    for v in graph[s]:
        if not visited[v]:
            path[v] = s
            DFSRecursion(v)



