""" Letter Combinations of a Phone Number """

class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        ans = []
        cdic = {1:[]}
        a = 'abcdefghijklmnopqrstuvwxyz'
        j = 0
        for i in range(2,7):
            if j < len(a):
                cdic[i] = [a[j],a[j+1],a[j+2]]
                j += 3
        
        cdic[7] = ['p','q','r','s']
        cdic[8] = ['t','u','v']
        cdic[9] = ['w','x','y','z']

        def dfs(snum, pr):
            if not snum:
                ans.append(pr)
                return
            for i in cdic[int(snum[0])]:
                dfs(snum[1:],pr+i)
        
        dfs(digits,'')
        return ans




            
s = Solution()
print(s.letterCombinations('23'))