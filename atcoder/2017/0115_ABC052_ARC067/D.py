# python3 (3.4.3)
import sys
input = sys.stdin.readline

# main
N,A,B = map(int,input().split())
X = list(map(int,input().split()))

ans = 0
for i in range(N-1):
    ans += min(B, A*(X[i+1]-X[i]))

print(ans)