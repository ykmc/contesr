# atcoder : python3 (3.4.3)
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
mod = 10**9+7

# main
N = int(input())
TXY = [[0,0,0]]+[list(map(int,input().split())) for _ in range(N)]

ans = "Yes"
for i in range(N):
    t0,x0,y0 = TXY[i]
    t1,x1,y1 = TXY[i+1]
    t = t1-t0
    d = abs(x1-x0)+abs(y1-y0)
    if t<d or d%2!=t%2:
        ans = "No"
        break

print(ans)