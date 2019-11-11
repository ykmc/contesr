# python3 (3.4.3)
import sys
input = sys.stdin.readline

# main
H,W = map(int,input().split())
C = [input().rstrip() for _ in range(H)]

for c in C:
    print(c)
    print(c)