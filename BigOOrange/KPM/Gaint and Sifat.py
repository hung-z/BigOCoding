def KMPpreprocess(P, prefix):
    prefix[0] = 0
    m = len(P)
    j = 0
    i = 1
    while i < m:
        if P[i] == P[j]:
            j += 1
            prefix[i] = j
            i += 1
        else:
            if j != 0:
                j = prefix[j - 1]
            else:
                prefix[i] = 0
                i += 1

def KPMSearch(T, P, prefix):
    n = len(T)
    m = len(P)
    i = j = 0
    count = 0
    while i < n:
        if T[i] == P[j]:
            i += 1
            j += 1
        if j == m:
            count += 1
            j = prefix[j - 1]
        elif i < n and T[i] != P[j]:
            if j != 0:
                j = prefix[j - 1]
            else:
                i += 1
    return count

T = int(input())
results = []
for i in range(T):
    T = input().replace(' ', '')
    P = input().replace(' ', '')
    prefix = [0] * len(P)
    KMPpreprocess(P, prefix)
    count = KPMSearch(T, P, prefix)
    results.append(count)
for i, result in enumerate(results):
    print("Case "+str(i+1)+": "+str(result))
    


