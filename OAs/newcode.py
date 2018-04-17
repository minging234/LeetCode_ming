import sys
if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    li = []
    ans = []
    linum = []

    for i in range(n):
        line = sys.stdin.readline().strip()
        values = list(map(int, line.split()))
        linum.append(values[0])
        li.append(values[1:]) 
    
    print(li,linum,ans,n)

    for ind in range(len(li)):
        diff = []
        T = 1
        flag = False
        for i in range(1,linum[ind]):
            diff.append(li[ind][i] - li[ind][i-1])
        print(diff)
        for step in range(1,len(diff)):
            j = 1
            while j < len(diff) - step:
                if diff[j] != diff[j+step]:
                    break
                j += 1
            if j == len(diff) - step:
                flag = True
                T = step
                break
            print('---',step)
        if flag == False:
            ans.append(sum(diff))
        else:
            ans.append(T)
    print( '---', ans)
    for a in ans:
        print(a)


                
