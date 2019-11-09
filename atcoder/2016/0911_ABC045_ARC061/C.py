# python3 (3.4.3)
import sys
input = sys.stdin.readline

# main
from itertools import product
S = input().rstrip()

ans = 0
ops = list(product("+ ", repeat=len(S)-1))

for op in ops:
    s = S[0] + "".join(x+y for (x,y) in zip(op,S[1::])).replace(" ","")
    ans += eval(s)

print(ans)