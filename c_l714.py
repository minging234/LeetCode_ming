

a = [2,1,4,4,2,3,2,5,1,2]


def maxProfit(prices, fee):
    """
    :type prices: List[int]
    :type fee: int
    :rtype: int
    """

    info = sunlist(prices,fee)
    # print(info)
    if info[0] <= 0:
        return 0

    l = info[1]
    r = info[2]
    if r == len(prices)-1:
        profit = info[0]
    else:
        profit = maxProfit(prices[:l],fee) + info[0] + maxProfit(prices[r:],fee)

    print(profit)

    i = r - 1

    while i > l:
        incre = max(prices[l:r]) - prices[i] - fee
        if incre > 0:
            profit += incre
            print(incre, i, prices[i])
            r = prices.index(max(prices[l:i]))
        i -= 1

    return profit


def sunlist(prices,fee):
    cm = 0
    l = 0
    r = 0

    for i in range(1, len(prices)):
        l = prices.index(min(prices[:i]))
        if prices[i] >= max(prices[l:i]):
            c = prices[i] - min(prices[:i])

            if c > cm:
                cm = c
                l = prices.index(min(prices[:i]))
                r = i
    if cm - fee < 0:
        return [0, l, r]
    return [cm - fee, l, r]


print(maxProfit(a,1))

# b = prices[0]
#
# for i in range(1, len(prices)):
#     b = min(b, prices[i])
#     cm = max(cm, prices[i] - b)
#
# if cm - fee < 0:
#     cm = 0
# else:
#     cm = cm - fee
#
# l = prices.index(b)
# r = prices.index(b + cm)

