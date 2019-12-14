# atcoder : python3 (3.4.3)
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# main
Xa,Ya,Xb,Yb,Xc,Yc = map(int,input().split())

Xb -= Xa
Xc -= Xa
Yb -= Ya
Yc -= Ya

print(abs(Xb*Yc - Xc*Yb)/2)