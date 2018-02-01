""" Word Break """

class Solution:
    dic = {}
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if not s:
            return True
        if s in self.dic:
            return self.dic[s]
        flag = False
        for i in range(1,len(s)+1):
            if s[:i] in wordDict:
                flag = flag or self.wordBreak(s[i:],wordDict)
        self.dic[(s)] = flag
        return flag

s = Solution()
print(s.wordBreak("aaaaaaa",["aaaa","aa"]))

"""
    总是只想到递归的方法，对于dp还是不能熟练运用，以下是dp的代码

        if not wordDict: return False
        dic = set(wordDict)
        lenset = set([len(word) for word in dic])
        check = [False] * (len(s)+1)
        check[0]=True
        for i in range(len(s)):
            for l in lenset:
                j = i-l+1
                if j <0:
                    continue
                if s[j:i+1] in dic and check[j]==True:
                    check[i+1]=True
                    break
        return check[-1]
    
"""