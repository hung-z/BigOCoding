from queue import Queue
MOD = 100000
MAX = MOD + 5
dist = [-1 for i in range(MAX)]

def BFS(s, lock):
    q = Queue()
    q.put(s)
    dist[s] = 0
    while not q.empty():
        u = q.get()
        for key in other_keys:
            v = (u*key) % MOD
            if(dist[v]==-1):
                dist[v] = dist[u] + 1
                q.put(v)
                if(v==lock):
                    return dist[v]
    return -1

key, lock = map(int, input().split())
num_keys = int(input())
other_keys = list(map(int, input().split()))
print(BFS(key, lock))
