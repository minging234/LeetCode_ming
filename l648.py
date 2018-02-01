""" Replace Words """

class Solution:
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        ans = ""
        rdic = {}
        start = float('inf')
        end = 0
        for i in dict:
            rdic[i] = 1
            start = min(len(i),start)
            end = max(len(i),end)

        words = sentence.split(' ')
        for word in words:
            for j in range(start,end+1):
                if word[:j] in rdic:
                    word = word[:j]
            ans += " " + word
        return ans[1:]

s = Solution()
print(s.replaceWords(["cat", "bat", "rat"],"the cattle was rattled by the battery"))
