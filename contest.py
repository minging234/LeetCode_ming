class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        ans = []
        def helper(s,pre):
            if not s:
                ans.append(pre)
                return
            if s[0] in "1234567890":
                helper(s[1:],pre+s[0])
            elif s[0] in "abcdefghijklmnopqrstuvwxyz":
                helper(s[1:],pre+s[0])
                helper(s[1:],pre+s[0].upper())
            else:
                helper(s[1:],pre+s[0])
                helper(s[1:],pre+s[0].lower())
        helper(s,"")
        return ans


    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        if not graph:
            return True      
        def helper(ind, dic1, dic2):
            if ind == len(graph):
                return True      
            if len(dic1 & dic2) != 0:
                return False
            if ind in dic1:
                dic2.update(graph[ind])
                return helper(ind+1,dic1,dic2)
            elif ind in dic2:
                dic1.update(graph[ind])
                return helper(ind+1,dic1,dic2)
            else:
                ndic1, ndic2 = dic1.copy(), dic2.copy()
                dic1.add(ind)
                dic2.update(graph[ind])
                ndic2.add(ind)
                ndic1.update(graph[ind])
                return helper(ind+1,dic1,dic2) or helper(ind+1, ndic1,ndic2)
 
        dic1 = set([0])
        dic2 = set(graph[0])

        return helper(1,dic1,dic2)


    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        ans = []
        def bfs(s,citys):
            if s > K:
                return
            tmp = {}
            for i in citys.keys():
                for j in flights:
                    if j[0] == i:
                        tmp[j[1]] = j[2]+citys[i] if j[1] not in tmp else min(tmp[j[1]],j[2]+citys[i])
            if dst in tmp:
                ans.append(tmp[dst])
            bfs(s+1,tmp)

        bfs(0,{src:0})

        return min(ans) if ans else -1
            








        

s = Solution()
# print(s.isBipartite([[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]]))
print(s.findCheapestPrice(17,
[[0,12,28],[5,6,39],[8,6,59],[13,15,7],[13,12,38],[10,12,35],[15,3,23],[7,11,26],[9,4,65],[10,2,38],[4,7,7],[14,15,31],[2,12,44],[8,10,34],[13,6,29],[5,14,89],[11,16,13],[7,3,46],[10,15,19],[12,4,58],[13,16,11],[16,4,76],[2,0,12],[15,0,22],[16,12,13],[7,1,29],[7,14,100],[16,1,14],[9,6,74],[11,1,73],[2,11,60],[10,11,85],[2,5,49],[3,4,17],[4,9,77],[16,3,47],[15,6,78],[14,1,90],[10,5,95],[1,11,30],[11,0,37],[10,4,86],[0,8,57],[6,14,68],[16,8,3],[13,0,65],[2,13,6],[5,13,5],[8,11,31],[6,10,20],[6,2,33],[9,1,3],[14,9,58],[12,3,19],[11,2,74],[12,14,48],[16,11,100],[3,12,38],[12,13,77],[10,9,99],[15,13,98],[15,12,71],[1,4,28],[7,0,83],[3,5,100],[8,9,14],[15,11,57],[3,6,65],[1,3,45],[14,7,74],[2,10,39],[4,8,73],[13,5,77],[10,0,43],[12,9,92],[8,2,26],[1,7,7],[9,12,10],[13,11,64],[8,13,80],[6,12,74],[9,7,35],[0,15,48],[3,7,87],[16,9,42],[5,16,64],[4,5,65],[15,14,70],[12,0,13],[16,14,52],[3,10,80],[14,11,85],[15,2,77],[4,11,19],[2,7,49],[10,7,78],[14,6,84],[13,7,50],[11,6,75],[5,10,46],[13,8,43],[9,10,49],[7,12,64],[0,10,76],[5,9,77],[8,3,28],[11,9,28],[12,16,87],[12,6,24],[9,15,94],[5,7,77],[4,10,18],[7,2,11],[9,5,41]]
,13
,4
,13))
                    