from math import ceil, log2
INF = 10**9

def updateQuery(segtree, a, left, right, index, pos, value):
    if pos < left or right < pos:
        return
    if left == right:
        a[pos] = value
        segtree[index] = value
        return
    mid = (left + right)/2
    if pos <= mid:
        updateQuery(segtree, a, left, mid, 2*index + 1, pos, value)
    else:
        updateQuery(segtree, a, mid + 1, right, 2 * index + 2, pos, value)
    segtree[index] = segtree[2 * index + 1] + segtree[2 * index + 2]

def sumRange(segtree, left, right, fr, to, index):
    if fr <= left and to >= right:
        return segtree[index]
    if fr > right or to < left:
        return 0
    mid = (left + right)//2
    return sumRange(segtree, left,  mid, fr, to, 2 * index + 1) + sumRange(segtree, mid+1, right, fr, to, 2 * index + 2)

def buildtree(a, segtree, left, right, index):
    if left == right:
        segtree[index] = a[left]
        return
    mid = (left + right)//2
    buildtree(a, segtree, left, mid, 2 * index + 1)
    buildtree(a, segtree, mid + 1, right, 2 * index + 2)
    segtree[index] = segtree[2 * index + 1] + segtree[2 * index + 2]

T = int(input())
results = []
for i in range(T):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    h = ceil(log2(len(a)))
    sizeTree = 2 * (2**h) - 1
    segtree = [INF] * sizeTree
    lazy = [0]*sizeTree
    buildtree(a, segtree, 0, len(a)-1, 0)
    sumranges = []
    for j in range(q):
        query = list(map(int, input().split()))
        query_type = query[0]
        if(query_type == 1):
            position = query[1]
            updateQuery(segtree, a, 0, len(a)-1, 0, position, 0)
        elif(query_type == 2):
            ith, v = query[1], query[2]
            updateQuery(segtree, a, 0, len(a)-1, 0, ith, v)
        elif(query_type == 3):
            fr, to = query[1], query[2]
            sumranges.append(sumRange(segtree, 0, len(a)-1, fr, to, 0))
    results.append(sumranges)

for i, result in enumerate(results):
    print("Case "+str(i+1)+":")
    for number in result:
        print(number)


