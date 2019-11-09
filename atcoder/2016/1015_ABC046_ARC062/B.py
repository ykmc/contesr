# python3 (3.4.3)
import sys
input = sys.stdin.readline

# main
N,K = map(int,input().split())

ans = K
for i in range(1,N):
    ans *= K-1

print(ans)