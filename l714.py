""" Best Time to Buy and Sell Stock with Transaction Fee """

class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        cash = 0
        hold = -prices[0]
        for i in range(1,len(prices)):
            cash = max(cash, hold + prices[i] - fee)
            hold = max(hold, cash -prices[i])
            print("----",cash,hold)
        return cash


s = Solution()
print(s.maxProfit([1,5,5,4,8,10,15],2))

""" 
    一个不是dp的方法

        prices.append(0) 
        total_profit = 0

        cur_min = prices[0]
        cur_max = prices[0]

        for price in prices:
            if price > cur_max:
                cur_max = price
            else:               
                if cur_max - price > fee:
                    profit = cur_max - cur_min - fee
                    if profit > 0:
                        total_profit += profit
                    cur_min = price
                    cur_max = price
                if price < cur_min:
                    cur_min = price
                
        return total_profit
"""
