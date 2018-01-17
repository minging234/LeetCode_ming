"""Best Time to Buy and Sell Stock II"""

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        pmax = 0
        sell = 0
        buy = float('inf')
        flag = 0
        i = 0
        if len(prices) == 1:
            return 0

        for i in range(len(prices)):
            if i == 0:
                if prices[i] <= prices[i+1]:
                    buy = prices[i]
                    flag = 1
            elif i == len(prices)-1:
                if prices[len(prices)-1] >= prices[len(prices)-2]:
                    sell = prices[len(prices)-1]
                    if buy < sell and flag == 1:
                        pmax += sell - buy
                        flag = 0 
                        print(sell - buy, sell, buy)                   

            elif prices[i] < prices[i+1] and prices[i-1] >= prices[i]:
                buy = prices[i]
                flag = 1

            elif prices[i] >= prices[i+1] and prices[i-1] < prices[i]:
                sell = prices[i]
                if buy < sell and flag == 1:
                    pmax += sell - buy
                    flag = 0
                    print(sell - buy, sell, buy)   
        return pmax


a = Solution()
print (a.maxProfit([2,9,2,3,8,1,5,8,4,3,6,4,4]))



"""
我的方法有点蠢，考虑的情况太多了，而且，这个极值找的方法也不对，特别容易出错
this is the good answer of Java

class Solution {
    public int maxProfit(int[] prices) {
        int maxprofit = 0;
        for (int i = 1; i < prices.length; i++) {
            if (prices[i] > prices[i - 1])
                maxprofit += prices[i] - prices[i - 1];
        }
        return maxprofit;
    }
}


"""

