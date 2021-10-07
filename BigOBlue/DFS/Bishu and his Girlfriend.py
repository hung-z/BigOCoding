MAX = 1005
V = None
E = None
INF = 10000
visited = [False for i in range(MAX)]
path = [0 for i in range(MAX)]
graph = [[] for i in range(MAX)]
dist = [0 for i in range(MAX)]

def DFS(src):
    for i in range(V):
        visited[i] = False
        path[i] = -1
    s = []
    visited[src] = True
    s.append(src)
    while len(s) > 0:
        u = s.pop()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                s.append(v)
                path[v] = u
                if(dist[v]==0):
                    dist[v] = dist[u] + 1

V = int(input())
for i in range(V-1):
    u, v = map(int, input().split())
    u, v = u-1, v-1
    graph[u].append(v)
    graph[v].append(u)
DFS(0)
Q = int(input())
girls = []
min_distance = INF
girl_country = -1
for i in range(Q):
    girl = int(input()) - 1
    girls.append(girl)
girls= sorted(girls)
for girl in girls:
    if dist[girl] < min_distance:
        min_distance = dist[girl]
        girl_country = girl
print(girl_country+1)
