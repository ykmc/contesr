# python3 (3.4.3)
import sys
input = sys.stdin.readline

# main
A,B,X = map(int,input().split())

print(B//X - (A-1)//X)