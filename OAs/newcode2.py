#coding=utf-8
import sys
if __name__ == "__main__":
    # 读取第一行的n

    line = sys.stdin.readline().strip()
    n1, n2, m = list(map(int, line.split()))
    line = sys.stdin.readline().strip()
    normal = list(map(int, line.split()))
    line = sys.stdin.readline().strip()
    scoin = list(map(int, line.split()))

    ans = 0
    ansdict = {}

    def dfs(curr, n1, n2, m, sctag, nortag):
        global ans
        global ansdict
        if curr == m:
            st = tuple(nortag + sctag)
            if st in ansdict:
                return
            ans += 1
            ansdict[st] = 1
            return
        if curr > m:
            return
        for i in range(n1):
            nortag[i] += 1
            dfs(curr+normal[i],n1,n2,m, sctag, nortag)
            nortag[i] -= 1
        for j in range(n2):
            if sctag[j] == 0:
                continue
            sctag[j] = 0
            dfs(curr+scoin[j],n1,n2,m, sctag, nortag)
            sctag[j] = 1
        return
    dfs(0,n1,n2,m,[1]*n2, [0]*n1)
    
    print(ans)
