# python3 (3.4.3)
import sys
input = sys.stdin.readline

# main
A,B = map(int,input().split())

print((A+B)%24)