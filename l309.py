""" Best Time to Buy and Sell Stock with Cooldown """

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        if len(prices) == 2:
            return prices[1]-prices[0] if prices[1]-prices[0] > 0 else 0

        hold = [-prices[0]]
        sold = [0]

        hold.append(max(hold[0],0-prices[1]))
        sold.append(max(sold[0],hold[0]+prices[1]))

        for i in range(2,len(prices)):
            hold.append(max(hold[i-1],sold[i-2]-prices[i]))
            sold.append(max(sold[i-1],hold[i-1]+prices[i]))
        
        return sold[-1]
