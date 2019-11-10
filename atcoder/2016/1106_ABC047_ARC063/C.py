# python3 (3.4.3)
import sys
input = sys.stdin.readline

# main
S = input().rstrip()

ans = 0
for i in range(1,len(S)):
    if S[i]!=S[i-1]:
        ans += 1

print(ans)