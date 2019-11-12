# python3 (3.4.3)
import sys
input = sys.stdin.readline

# main
A,op,B = input().split()

print(eval(A+op+B))