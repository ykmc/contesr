# python3 (3.4.3)
import sys
input = sys.stdin.readline

# main
S = input()

N = len(S)
ans = [-1,-1]

for i in range(N-1):
    if S[i]==S[i+1]:
        ans = [i+1,i+2]
        break

for i in range(N-2):
    if S[i]==S[i+2]:
        ans = [i+1, i+3]
        break

print(ans[0], ans[1])