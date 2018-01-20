""" Daily Temperatures """

class Solution(object):
    def dailyTemperatures(self, T):
        ans = [0] * len(T)
        stack = [] #indexes from hottest to coldest
        for i in range(len(T) - 1, -1, -1):
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()
            if stack:
                ans[i] = stack[-1] - i
            stack.append(i)
        return ans

s = Solution()
print(s.dailyTemperatures([73,74,75,71,69,72,76,73]))


"""
    最普通的超时的方法

        ans = []
        for i in range(len(temperatures)):
            j = i 
            wait = 0       
            while temperatures[j] <= temperatures[i]:
                wait += 1
                j += 1
                if j == len(temperatures):
                    wait = 0
                    break            
            ans.append(wait)
        return ans
"""    
                    