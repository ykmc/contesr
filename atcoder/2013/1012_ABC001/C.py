# python3 (3.4.3)
import sys
input = sys.stdin.readline

# main
DEG,DIS = map(int,input().split())

deg_i = ((DEG+112)//225)
deg_list = ["N","NNE","NE","ENE","E","ESE","SE","SSE","S","SSW","SW","WSW","W","WNW","NW","NNW","N"]

ans_deg = deg_list[deg_i]

ans_dis = 0
if DIS < 15:
    ans_dis = 0
elif DIS < 15*6+3:
    ans_dis = 1
elif DIS < 33*6+3:
    ans_dis = 2
elif DIS < 54*6+3:
    ans_dis = 3
elif DIS < 79*6+3:
    ans_dis = 4
elif DIS < 107*6+3:
    ans_dis = 5
elif DIS < 138*6+3:
    ans_dis = 6
elif DIS < 171*6+3:
    ans_dis = 7
elif DIS < 207*6+3:
    ans_dis = 8
elif DIS < 244*6+3:
    ans_dis = 9
elif DIS < 284*6+3:
    ans_dis = 10
elif DIS < 326*6+3:
    ans_dis = 11
else:
    ans_dis = 12

if ans_dis == 0:
    ans_deg = "C"

print(ans_deg, ans_dis)