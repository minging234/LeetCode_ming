""" Coin Change """

class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """  
        self.res = float("inf")
        coins.sort(reverse=True)
        self.DFS(coins, amount, 0, 0)
        return self.res if self.res < float("inf") else -1

    def DFS(self, coins, amount, count, index):
        if amount == 0:
            self.res=min(self.res, count)
            return
        if amount < 0:
            return
        for i in range(index, len(coins)):
            if coins[i] <= amount < coins[i] * (self.res - count):
                self.DFS(coins, amount-coins[i], count+1, i)


s = Solution()
print(s.coinChange([1, 2, 5],11))


""" 
    使用的 递归的方法，结果超时了，感觉和答案的思路是一样的

        cdic = {}

        def dfs(m):
            if m < 0:
                return -1
            if m == 0:
                return 0
            if m in cdic:
                return cdic[m]
            pn = float('inf')
            for i in range(len(coins)):
                chd = dfs(m-coins[i])
                if chd != -1:
                    pn = min(pn, chd)
            pn += 1
            if pn != float('inf'):
                cdic[m] = pn
                return pn
            cdic[m] = -1
            return -1

        return dfs(amount)

    下面是使用迭代的方法，同样超时，看来是python的问题

        dp = [amount + 1]*(amount+1)
        dp[0] = 0
        for i in range(amount+1):
            for j in coins:
                if j <= i:
                    dp[i] = min(dp[i],dp[i-j]+1)

        return dp[amount] if dp[amount] <= amount else -1

"""

        