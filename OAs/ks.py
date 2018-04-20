#coding=utf-8
import sys 
for line in sys.stdin:
    a = line.split()
    x = int(a[0])
    y = int(a[1])
    N = int(a[2])
    
    def helper(x,y,N):
        if y == 1:
            return x%N
        if y == 0:
            return 1
        sp = y//2
        lf = y%2
        midout = helper(x, sp, N)
        midout *= midout
        if lf == 1:
            midout *= x
        return midout%N
    print(helper(x,y,N))

