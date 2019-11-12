# python3 (3.4.3)
import sys
input = sys.stdin.readline

# main
N = int(input())
S = input().rstrip()

ans = 0
total = 0
for s in S:
    if s=="I":
        total += 1
    else:
        total -= 1
    ans = max(ans,total)

print(ans)