# python3 (3.4.3)
import sys
input = sys.stdin.readline

# main
M = int(input())

ans = 0
if M < 100:
    ans = 0
elif M <= 5000:
    ans = M//100
elif M <= 30000:
    ans = M//1000 + 50
elif M <= 70000:
    ans = (M//1000-30)//5 + 80
else:
    ans = 89

print("{0:02d}".format(ans))