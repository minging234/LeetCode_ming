
def maxProfit(prices):
    pmax = 0
    buy = float('Inf')
    sell = 0

    for i in prices:
        if i < buy:
            buy = i
            sell = 0
        elif i > sell:
            sell = i
        a = sell - buy
        if a > pmax:
            pmax = a

    return pmax




a = [7, 6, 4, 3, 1]

print(maxProfit(a))