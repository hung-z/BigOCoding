N = int(input())
bit = list(map(int, input().split()))
prefix_sums = [0 for i in range(len(bit))]
for i in range(len(bit)):
    if(i==0):
        prefix_sums[i] = bit[i]
    else:
        prefix_sums[i] = prefix_sums[i-1] + bit[i]
Q = int(input())
results = []
for i in range(Q):
    L, R = map(int, input().split())
    L, R = L - 1, R - 1
    if(L==0):
        no1 = prefix_sums[R] - 0
    else:
        no1 = prefix_sums[R] - prefix_sums[L-1]
    xorValue = no1 & 1
    no0 = R - L + 1 - no1
    results.append(str(xorValue)+" "+str(no0))
for result in results:
    print(result)
