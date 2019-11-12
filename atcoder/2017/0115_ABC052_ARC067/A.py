# python3 (3.4.3)
import sys
input = sys.stdin.readline

# main
A,B,C,D = map(int,input().split())

print(max(A*B,C*D))