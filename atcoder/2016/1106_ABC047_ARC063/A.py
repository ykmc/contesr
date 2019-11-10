# python3 (3.4.3)
import sys
input = sys.stdin.readline

# main
ABC = list(map(int,input().split()))

ABC.sort()

print("Yes" if ABC[0]+ABC[1]==ABC[2] else "No")