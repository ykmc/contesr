# python3 (3.4.3)
import sys
input = sys.stdin.readline

# main
W,H,N = map(int,input().split())
XYA = [list(map(int,input().split())) for _ in range(N)]

x_lb,x_ub,y_lb,y_ub = 0,W,0,H

for x,y,a in XYA:
    if a==1:
        x_lb = max(x_lb,x)
    elif a==2:
        x_ub = min(x_ub,x)
    elif a==3:
        y_lb = max(y_lb,y)
    else:
        y_ub = min(y_ub,y)

x = max(0, x_ub - x_lb)
y = max(0, y_ub - y_lb)

print(x*y)