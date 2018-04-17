class Solution:
    def similarRGB(self, color):
        """
        :type color: str
        :rtype: str
        """
        ans = '#'
        for i in range(1,7,2):
            num = int(color[i:i+2],16)
            char = ''
            mind = float('inf')
            for j in range(16):
                dis = abs(j*16 + j - num)
                if dis < mind:
                    mind = dis
                    char = j
            ans += str(hex(char))[2:] + str(hex(char))[2:]
        return ans


    def minSwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        M = [0] * len(A)
        N = [0] * len(A)
        N[0] = 1
        for i in range(1,len(A)):
            if A[i] > A[i-1] and B[i] > B[i-1]:
                if A[i] > B[i-1] and B[i] > A[i-1]:
                    M[i] = min(M[i-1],N[i-1])
                    N[i] = min(M[i-1],N[i-1])+1
                else:
                    M[i] = M[i-1]
                    N[i] = N[i-1]+1
            else:
                M[i] = N[i-1]
                N[i] = M[i-1]+1
        
        return min(M[-1],N[-1])


        


s = Solution()
print(s.similarRGB("#09f166"))