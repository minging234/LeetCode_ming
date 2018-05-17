import sys

if __name__ == "__main__":
    line = sys.stdin.readline().strip()
    n, w = list(map(int, line.split()))

    def helper(x,y):
        if y == 1:
            return x%100003
        if y == 0:
            return 1
        sp = y//2
        lf = y%2
        midout = helper(x, sp)
        midout *= midout
        if lf == 1:
            midout *= x
        return midout%100003
    
    total = helper(n,w)
    if w > 1:
        good = helper(n-1,w-1)*n % 100003
    else:
        good = n
    bad = (total - good)%100003
    print(bad)

    