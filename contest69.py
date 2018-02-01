class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        ans = 0
        jew = set(list(J))
        for i in range(len(S)):
            if S[i] in jew:
                ans += 1
        return ans

    def isIdealPermutation(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        pmax = A[0]
        for i in range(1,len(A)):
            if A[i] < pmax and A[i-1] != pmax:
                return False
            pmax = max(pmax,A[i-1])
        return True


    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        dic = [[],[]]
        import collections
        stack = collections.deque()
        stack.append(board)

        def bfs(bd,t):    
            a = []
            a.append(list(bd[0]))
            a.append(list(bd[1]))

            if a in dic[0]:
                return
            else:
                dic[0].append(a)  
                dic[1].append(t+1)
                a = []
                a.append(list(bd[0]))
                a.append(list(bd[1]))      
                stack.append(a) 
                return
        
        bfs(board,-1)

        while stack:
            bd = stack.popleft()
            t = dic[1][dic[0].index(bd)]
            if 0 in bd[0]:
                b = 0
            else:
                b = 1
            if bd[b].index(0) == 0:
                bd[b][0],bd[b][1] = bd[b][1],bd[b][0]
                bfs(bd,t)
                bd[b][0],bd[b][1] = bd[b][1],bd[b][0]
                bd[b][0],bd[1-b][0] = bd[1-b][0],bd[b][0]
                bfs(bd,t)
            elif bd[b].index(0) == 1:
                bd[b][0],bd[b][1] = bd[b][1],bd[b][0]
                bfs(bd,t)
                bd[b][0],bd[b][1] = bd[b][1],bd[b][0]
                bd[b][2],bd[b][1] = bd[b][1],bd[b][2]
                bfs(bd,t)
                bd[b][2],bd[b][1] = bd[b][1],bd[b][2]
                bd[b][1],bd[1-b][1] = bd[1-b][1],bd[b][1]
                bfs(bd,t)
            elif bd[b].index(0) == 2:
                bd[b][2],bd[b][1] = bd[b][1],bd[b][2]
                bfs(bd,t)
                bd[b][2],bd[b][1] = bd[b][1],bd[b][2]
                bd[b][2],bd[1-b][2] = bd[1-b][2],bd[b][2]
                bfs(bd,t)
            if [[1,2,3],[4,5,0]] in dic[0]:
                return dic[1][dic[0].index([[1,2,3],[4,5,0]])]
            
        return -1

    def minmaxGasDist(self, stations, K):
        """
        :type stations: List[int]
        :type K: int
        :rtype: float
        """
        dist = []
        cut = []
        gap = []

        for i in range(1,len(stations)):
            dist.append(stations[i]-stations[i-1])
        
        dist.sort(reverse=True)
        cut = [0] * len(dist)
        cut[0] = K
        gap.append(dist[0]/(cut[0]+1))

        for i in range(1,len(dist)):
            cur = dist[i]
            if cut[i-1] == 0:
                return max(gap)
            else:
                while cur > max(gap):
                    pre = max(max(gap),cur)
                    ming = min(gap)
                    ind = gap.index(ming)
                    if cut[ind] == 0:
                        break
                    cut[ind] -= 1
                    gap[ind] = dist[ind]/(cut[ind]+1)
                    cut[i] += 1
                    cur = dist[i]/(cut[i]+1)

            gap.append(cur)
            print(gap)    

            if max(gap) > pre:
                cut[i] -= 1
                cut[ind] += 1
                gap[ind] = dist[ind]/(cut[ind]+1)
                gap[i] = dist[i]/(cut[i]+1)
            print(gap, dist)
        return max(gap)




s = Solution()
# print(s.slidingPuzzle([[4,1,2],[5,0,3]]))
print(s.minmaxGasDist([12,17,54,66,77,83,88,92,97,99],6))