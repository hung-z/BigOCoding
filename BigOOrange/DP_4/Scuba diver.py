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
values = []
for i in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    sum_coins = sum(coins)
    W = sum_coins//2
    items = []
    items.append(Item(0,0))
    for coin in coins:
        item = Item(coin, coin)
        items.append(item)
    dp = []
    value = Knapsach(items, W)
    values.append(sum_coins - value*2)
for value in values:
    print(value)


