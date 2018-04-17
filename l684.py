""" Redundant Connection """
import collections

class DSU(object):
    def __init__(self):
        self.par = range(1001)
        self.rnk = [0] * 1001

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        elif self.rnk[xr] < self.rnk[yr]:
            self.par[xr] = yr
        elif self.rnk[xr] > self.rnk[yr]:
            self.par[yr] = xr
        else:
            self.par[yr] = xr
            self.rnk[xr] += 1
        return True


class Solution:
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        dsu = DSU()
        for edge in edges:
            if not dsu.union(*edge):
                return edge


        # if not edges:
        #     return None
        # neigbor = {}
        # for edge in edges:
        #     for i in range(2):
        #         if edge[i] not in neigbor:
        #             neigbor[edge[i]] = [edge[i-1]]
        #         else:
        #             neigbor[edge[i]].append(edge[i-1])


        # start = edges[0][0]
        # explored = {start:1}
        # que = collections.deque()
        # que.append(start)

        # while len(que) != 0:
        #     curr = que.popleft()
        #     for node in neigbor[curr]:         
        #         neigbor[node].remove(curr)
        #         if node not in explored:
        #             explored[node] = 1
        #             que.append(node)
        #         else:
        #             return [curr, node]
        # return None


                
S = Solution()
print(S.findRedundantConnection([[1,2],[1,3],[2,3]]))

        
