# python3 (3.4.3)
import sys
input = sys.stdin.readline

# main
from collections import Counter
S = input().rstrip()
T = int(input())

c = Counter(S)

x = c["R"] - c["L"]
y = c["U"] - c["D"]

ans = abs(x)+abs(y)
if T==1:
    ans += c["?"]
else:
    if ans > c["?"]:
        ans -= c["?"]
    else:
        ans = (ans-c["?"])%2

print(ans)