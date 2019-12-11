# atcoder : python3 (3.4.3)
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# main
W = input().rstrip()

ans = ""
for w in W:
    if w not in "aiueo":
        ans += w

print(ans)