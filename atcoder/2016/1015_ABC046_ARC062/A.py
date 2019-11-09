# python3 (3.4.3)
import sys
input = sys.stdin.readline

# main
A,B,C = map(int,input().split())

print(len({A,B,C}))