class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        def findpath(path,dest,ans):
            if path[-1] == dest:
                ans.append(path)
                return
            if path[-1] not in wordpath:
                return
            for i in wordpath[path[-1]]:
                newpath=list(path)
                newpath.append(i)
                findpath(newpath,dest,ans)       
            return
        

        length = 2
        if endWord not in wordList:
            return []
        wordpath = {}
        ans = []
        front, back, wordDict = set([beginWord]), set([endWord]), set(wordList)
        wordDict.discard(beginWord)
        
        for word in wordList:
            wordpath[word] = []
        
        while front:
            # generate all valid transformations
            temp = []
            for word in front:
                tmp = wordDict & (set(word[:index] + ch + word[index+1:] for index in range(len(beginWord)) for ch in 'abcdefghijklmnopqrstuvwxyz'))
                for i in tmp:
                    wordpath[i].append(word)
                temp += tmp
            front = set(temp)

            if front & back:
                # there are common elements in front and back, done
                for i in front & back:
                    ans1, ans2 = [],[]
                    findpath([i],endWord, ans1)
                    findpath([i],beginWord, ans2) 

                    for m in ans1:
                        for n in ans2:
                            ans.append(n[::-1]+ m[1:]) 
                print (wordpath)
                return ans
            
            length += 1
            if len(front) > len(back):
                # swap front and back for better performance (fewer choices in generating nextSet)
                front, back = back, front
            # remove transformations from wordDict to avoid cycle
            wordDict -= front
        
        return []

 
       
s = Solution()
print(s.findLadders("hit","cog",["hot","dot","dog","lot","log","cog"]))