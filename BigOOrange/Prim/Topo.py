def dfs(u, graph, visited, result):
    visited[u] = True
    for v in graph[u]:
        if not visited[u]:
            dfs(v, graph, visited, result)
    result.append(u)

def topologicalSort(graph, result):
    visited = [False] * V
    for i in range(V):
        if not visited[i]:
            dfs(i, graph, visited, result)
    result.reverse()

if __name__ == "__main__":
    V, E = map(int, input().split())
    graph = [[] for i in range(V)]
    result = []
    for i in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
    topologicalSort(graph, result)

