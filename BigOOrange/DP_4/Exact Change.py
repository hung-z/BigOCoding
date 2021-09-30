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

T = int(input())

