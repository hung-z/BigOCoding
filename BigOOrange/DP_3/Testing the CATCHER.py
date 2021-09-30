

def lowerBound(a, sub, n, x):
    left = 0
    right = n
    pos = right
    while left < right:
        mid = left + (right - left) // 2
        index = sub[mid]
        if a[index] <= x:
            pos = mid
            right = mid
        else:
            left = mid + 1
    return pos

def LIS(a):
    global path
    length = 1
    path = [-1] * len(a)
    dp.append(0)
    for i in range(1, len(a)):
        if a[i] >= a[dp[0]]:
            dp[0] = i
        elif a[i] <= a[dp[length - 1]]:
            path[i] = dp[length - 1]
            dp.append(i)
            length += 1
        else:
            pos = lowerBound(a, dp, length, a[i])
            path[i] = dp[pos - 1]
            dp[pos] = i
    return length

a = []
results = []
while(1):
    rocket_high = int(input())
    if(rocket_high == -1 and len(a)==0):
        break
    if(rocket_high!=-1):
        a.append(rocket_high)
    if(rocket_high == -1 and len(a)>0):
        dp = []
        sequence_len = LIS(a)
        results.append(sequence_len)
        a = []
        continue
for i, result in enumerate(results):
    print("Test #"+str(i+1)+':')
    print("  maximum possible interceptions: "+str(result))
