# python3 (3.4.3)
import sys
input = sys.stdin.readline

# main
S = input()

ans = ""
for s in S:
    if s=="B":
        ans = ans[:-1]
    else:
        ans += s

print(ans)
