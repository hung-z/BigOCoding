import queue
class Node:
    def __init__(self, id, dist):
        self.dist = dist
        self.id = id
    def __lt__(self, other):
        return self.dist <= other.dist

def lenMST():
    ans = 0
    for i in range(n):
        if path[i] == -1:
            continue
        ans+=dist[i]
    return ans

def prims(src):
    pq = queue.PriorityQueue()
    pq.put(Node(src, 0))
    dist[src] = 0
    while pq.empty() == False:
        top = pq.get()
        u  = top.id
        visited[u] = True
        for neighbor in graph[u]:
            v = neighbor.id
            w = neighbor.dist
            if visited[v] == False and w < dist[v]:
                dist[v] = w
                pq.put(Node(v, w))
                path[v] = u

def printMST():
    ans = 0
    for i in range(n):
        if path[i] == -1:
            continue
        ans+=dist[i]
        print("{0} - {1}: {2}".format(path[i], i, dist[i]))
    print("Weight of MST: {0}".format(ans))



INF = 1e9
num_tests = int(input())
results = []
for i in range(num_tests):
    n, m = map(int, input().split())
    graph = [[] for i in range(n)]
    dist = [INF for i in range(n)]
    path = [-1 for i in range(n)]
    visited = [False for i in range(n)]
    for j in range(m):
        u, v, w = map(int, input().split())
        graph[u-1].append(Node(v-1, w))
        graph[v-1].append(Node(u-1, w))
    prims(0)
    # printMST()
    price_1 = lenMST()
    ### Assign smallest edge to INF
    min_value = INF
    min_vertex = 0
    min_source_vertex = 0
    for j in range(1, len(dist)):
        if(dist[j]<min_value):
            min_value = dist[j]
            min_vertex = j
            min_source_vertex = path[j]
    # print(min_value, min_vertex, min_source_vertex,"------")
    for j in range(len(graph[min_source_vertex])):
        node = graph[min_source_vertex][j]
        if(node.id == min_vertex):
            graph[min_source_vertex][j].dist = INF
    for j in range(len(graph[min_vertex])):
        node = graph[min_vertex][j]
        if(node.id == min_source_vertex):
            graph[min_vertex][j].dist = INF
    # for node in graph[min_source_vertex]:
    #     print("----", node.id, node.dist)
    # print("************************")
    # for node in graph[min_vertex]:
    #     print("----", node.id, node.dist)
    dist = [INF for i in range(n)]
    path = [-1 for i in range(n)]
    visited = [False for i in range(n)]
    prims(0)
    price_2 = lenMST()
    results.append((price_1, price_2))
for result in results:
    print(str(result[0])+" "+str(result[1]))



