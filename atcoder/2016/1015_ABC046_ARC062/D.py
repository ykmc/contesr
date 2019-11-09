# python3 (3.4.3)
import sys
input = sys.stdin.readline

# main
S = input().rstrip()

ans = 0
for i in range(len(S)):
    if i%2==0 and S[i]=="p":
        ans -= 1
    elif i%2==1 and S[i]=="g":
        ans += 1

print(ans)
