#coding=utf-8
import sys 

a = sys.stdin.readline().strip()
A = list(map(int, a.split()))
x = int(sys.stdin.readline().strip())

ans = 0

if not A or len(A)==0:
    ans = 0
    print(ans)
else:

    start = 0
    end = len(A)-1

    while start + 1 < end:
        mid = start + (end - start) // 2

        if A[mid] == x:
            end = mid
        elif A[mid] < x:
            start = mid
        else:
            end = mid

    if ans != 0:
        print(ans)
    else:
        if A[start] == x:
            print(start)
        elif A[end] == x:
            print(end)
        else:
            if A[start] > x:
                print(start)
            elif A[end] < x:
                print(len(A))
            else:
                print(end)
    