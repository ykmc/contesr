# python3 (3.4.3)
import sys
input = sys.stdin.readline

# main
N,H = map(int,input().split())
A,B = 0,[]
for i in range(N):
    a,b = map(int,input().split())
    A = max(A,a)
    B.append(b)

ans = 0

B.sort(reverse=True)
for b in B:
    if b > A:
        ans += 1
        H -= b
        if H <= 0:
            print(ans)
            sys.exit()
            
print(ans + (H-1)//A + 1)