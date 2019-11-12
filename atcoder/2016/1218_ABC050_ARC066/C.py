# python3 (3.4.3)
import sys
input = sys.stdin.readline

# main
from collections import Counter
N = int(input())
A = list(map(int,input().split()))
mod = 10**9+7

C = dict(Counter(A))

ans = 1
if N%2==0:
    for i in range(N//2):
        if C.get(i*2+1) == 2:
            ans *= 2
            ans %= mod
        else:
            ans = 0
            break
else:
    if C[0] == 1:
        for i in range(N//2):
            if C.get(i*2+2) == 2:
                ans *= 2
                ans %= mod
            else:
                ans = 0
                break
    else:
        ans = 0

print(ans)