class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        if not matrix:
            return True
        def valid(w, h):
            val = matrix[w][h]
            while w < len(matrix) and h < len(matrix[0]):
                if matrix[w][h] != val:
                    return False
                w += 1
                h += 1
            return True

        for i in range(len(matrix[0])):
            if not valid(0,i):
                return False
        
        for j in range(len(matrix)):
            if not valid(j,0):
                return False
            
        return True

    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        if not S:
            return ""
        cdic = {}
        cmax = 0
        crest = 0
        fchar = ""
        for i in range(len(S)):
            if S[i] not in cdic:
                cdic[S[i]] = 1
            else:
                cdic[S[i]] += 1
        
        for num in cdic.items():
            if num[1] > cmax:
                crest += cmax
                cmax = num[1]
                fchar = num[0]                
            else:
                crest += num[1]
        if cmax >= crest + 2:
            return ""
        
        cdic[fchar] -= 1
        pr = fchar
        while len(fchar) < len(S): 
            for c in cdic.keys():
                if cdic[c] > 0 and c != pr:
                    fchar += c
                    cdic[c] -= 1
                    pr = c
        
        return fchar

        
        


    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        ordd = sorted(arr)
        ans = 0
        pa = {}
        p2 = 0
        for i in range(len(arr)):
            if arr[i] not in pa:
                pa[arr[i]] = 0
            else:
                pa[arr[i]] += 1
            p2 = max(p2, ordd.index(arr[i])+ pa[arr[i]])
            if i == p2:
                ans += 1              
        return ans



        

            



            


s = Solution()
# print(s.isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]]))
print( s.reorganizeString("sfffp"))
# print(s.maxChunksToSorted([1,1,0,0,1]))


"""
    第二题的dfs

        ans = []
        def find(last, vdic):
            vdic[last[-1]] -= 1
            if len(last) == len(S) :
                ans.append(last)
                return
            for i in vdic.keys():
                if i != last[-1] and vdic[i] > 0:
                    find(last + i,vdic)
            return 
        for ch in cdic.keys():
            find(ch,cdic)
            
        return ans[0]
    

    def reorganizeString(self, S):
    a = sorted(sorted(S), key=S.count)
    h = len(a) / 2
    a[1::2], a[::2] = a[:h], a[h:]
    return ''.join(a) * (a[-1:] != a[-2:-1])
"""