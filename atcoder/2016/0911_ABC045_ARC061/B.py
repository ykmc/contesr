# python3 (3.4.3)
import sys
input = sys.stdin.readline

# main
from collections import Counter
W = input().rstrip()

C = Counter(W)
ans = "Yes"
for v in C.values():
    if v%2 != 0:
        ans = "No"
        break

print(ans)