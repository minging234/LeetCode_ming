class Solution:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        a = A + A
        if B not in a:
            return False
        ind = a.index(B)
        c = a[:ind] + a[ind+len(B):]
        if A == c:
            return True
        else:
            return False


    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        ans = []

        def dfs(path, node):
            if node == len(graph) - 1:
                path.append(node)
                ans.append(path)
                return 
            if not graph[node]:
                return
            for newnode in graph[node]:
                newpath = list(path)
                newpath.append(node)
                dfs(newpath, newnode)
            return

        dfs([],0)

        return ans

    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        cups = []
        for i in range(query_row+1):
            cups.append([0]*(i+1))
        
        cups[0][0] = poured
        
        for i in range(query_row):
            for j in range(len(cups[i])):
                if cups[i][j] > 1:
                    cups[i+1][j] += (cups[i][j] - 1)/2
                    cups[i+1][j+1] += (cups[i][j] - 1)/2
        
        return cups[query_row][query_glass] if cups[query_row][query_glass] < 1 else 1
            
        
    def bestRotation(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        N = len(A)
        bad = [0] * N
        for i, x in enumerate(A):
            left, right = (i - x + 1) % N, (i + 1) % N
            print(left, right)
            bad[left] -= 1
            bad[right] += 1
            if left > right:
                bad[0] -= 1

        print(bad)

        best = -N
        ans = cur = 0
        for i, score in enumerate(bad):
            cur += score
            if cur > best:
                best = cur
                ans = i

        return ans






s = Solution()
# print(s.rotateString("abcde","cdeab"))
# print(s.champagneTower(1.5,1,1))
print(s.bestRotation([2, 3, 1, 4, 0]))