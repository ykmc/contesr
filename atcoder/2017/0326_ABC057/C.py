# python3 (3.4.3)
import sys
input = sys.stdin.readline

# functions
def F(a,b):
    return max(len(str(a)), len(str(b)))

# main
from collections import defaultdict
N = int(input())

ans = F(N,1)

divs = []
for i in range(1,int(N**.5)+1):
    if N%i==0:
        divs.append(i)

ans = len(str(N))
for d in divs:
    if N%d==0:
        ans = min(ans, F(d,N//d))

print(ans)