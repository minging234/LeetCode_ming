"""  Word Ladder """

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        length = 2
        front, back, wordDict = set([beginWord]), set([endWord]), set(wordList)
        wordDict.discard(beginWord)
        while front:
            # generate all valid transformations
            front = wordDict & (set(word[:index] + ch + word[index+1:] for word in front 
                                for index in range(len(beginWord)) for ch in 'abcdefghijklmnopqrstuvwxyz'))
            if front & back:
                # there are common elements in front and back, done
                return length
            length += 1
            if len(front) > len(back):
                # swap front and back for better performance (fewer choices in generating nextSet)
                front, back = back, front
            # remove transformations from wordDict to avoid cycle
            wordDict -= front
        return 0

s = Solution()
print(s.ladderLength("hit","cog", ["hot","dot","dog","lot","log","cog"]))


""" 
    想到的是用 dfs的方法，结果超时了，应该使用 BFS 的方法
            
        def search(midword, wordic, count):
            if midword == endWord:
                return count
            ndic = list(wordic)
            step = float('inf')
            for word in wordic:
                if compare(word, midword):
                    ndic.remove(word)
                    step = min(search(word, ndic, count+1),step)
            return step
        
        def compare(w1, w2):
            flag = 1
            for i in range(len(w1)):
                if w1[i] != w2[i]:
                    flag -= 1
                if flag < 0:
                    return False
            return True

        a = search(beginWord, wordList, 1)
        if a > len(wordList):
            return 0
        else:
            return a

"""


