class Item:
    def __init__(self, profit = 0, weight = 0):
        self.profit = profit
        self.weight = weight
dp = []
def Knapsach(items, W):
    global dp
    dp = [[0] * (W+1) for i in items]
    for i in range(1, len(items)):
        for j in range(W + 1):
            if items[i].weight > j:
                dp[i][j] = dp[i - 1][j]
            else:
                temp1 = items[i].profit + dp[i - 1][j - items[i].weight]
                temp2 = dp[i - 1][j]
                dp[i][j] = max(temp1, temp2)
    return dp[len(items) - 1][W]
 

# items = [Item(0,0), Item(1,1), Item(2,1), Item(2,2), Item(4,6), Item(10,4)]
# W = 10
# result = Knapsach(items, W)
# print("total value", result)
# exit()

T = int(input())
scores = []
for i in range(T):
    N, W = map(int, input().split())
    items = []
    items.append([0,0])
    for i in range(N):
        Ci, Pi, Ti = map(int, input().split())
        item = Item(Ci*Pi, Ti)
        items.append(item)
    # for item in items:
        # print(item.profit, item.weight)
    dp = []
    score = Knapsach(items, W)
    scores.append(score)
for score in scores:
    print(score)



