class Solution:
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        def helper(number):
            for i in range(10 - number%10):
                num = number + i
                if num <= n:
                    ans.append(num)
                    helper(num*10) 
                else:
                    break      
        ans = []
        helper(1)
        return ans



    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        chard = {}
        for i in range(len(s)):
            if s[i] in chard:
                chard[s[i]] += 1
            else:
                chard[s[i]] = 1
        
        for i in range(len(s)):
            if chard[s[i]] == 1:
                return i
        return -1


    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        if not input:
            return 0
        names = input.split('\n')
        stack = []
        ans = 0
        for name in names:
            pos = 0  
            while name.startswith('\t'):
                pos += 1
                name = name[1:]
            if len(stack) <= pos:
                stack.append("/" + name)
            else:
                while stack and len(stack) > pos:
                    stack.pop()
                stack.append("/" + name)
            if "." in name:
                if len("".join(stack))-1 > ans:
                    ans = len("".join(stack)) -1
        return ans
            


S = Solution()
print (S.lengthLongestPath("a\n\tb\n\t\tc.txt"))
            
