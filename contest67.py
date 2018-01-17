class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        total = 0
        prime = {2, 3, 5, 7, 11, 13, 17, 19}
        for i in range(L,R+1):
            sumi = 0
            while i != 0:
                if i & 1 == 1:
                    sumi += 1
                i = i >> 1
            if sumi in prime:
                total +=1
        return total


    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        dic = {}
        for i in range(len(S)):
            if S[i] in dic:
                dic[S[i]][1] = i 
            else:
                dic[S[i]] = [i,i]
        ordered = sorted(dic.values(), key=lambda b: b[0])
        
        start = 0
        end = 0
        ans = []

        for j in ordered:
            if j[0] <= end:
                if j[1] > end:
                    end = j[1]
            if j[0] > end:
                ans.append(end - start + 1)
                start = j[0]
                end = j[1]
        ans.append(end - start + 1)
        return ans


    def orderOfLargestPlusSign(self, N, mines):
        """
        :type N: int
        :type mines: List[List[int]]
        :rtype: int
        """
        maxs = 0
        mapn = [[1 for i in range(N)] for i in range(N)]
        for mine in mines:
            mapn[mine[0]][mine[1]] = 0

        def cons(w,l):
            if w-maxs < 0 or mapn[w-maxs][l] == 0:
                return 0
            if w+maxs > N-1 or mapn[w+maxs][l] == 0:
                return 0
            if l-maxs <0 or mapn[w][l-maxs] == 0:
                return 0
            if l+maxs > N-1 or mapn[w][l+maxs] == 0:
                return 0
            ps = 0
            while True:
                ps += 1
                if w-ps < 0 or mapn[w-ps][l] == 0:
                    break
                if w+ps > N-1 or mapn[w+ps][l] == 0:
                    break
                if l-ps <0 or mapn[w][l-ps] == 0:
                    break
                if l+ps > N-1 or mapn[w][l+ps] == 0:
                    break
            return ps

        for p in range(N):
            for q in range(N):
                if mapn[p][q] == 1:
                    maxs = max(maxs, cons(p,q))
        return maxs


s = Solution()
# print(s.partitionLabels("ababcbacadefegdehijhklij"))
print(s.orderOfLargestPlusSign(5,[[4, 2]]))




            