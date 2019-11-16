# python3 (3.4.3)
import sys
input = sys.stdin.readline

# function
import heapq
INF = float("inf")

def dijkstra(nodeNum, start, adjList):
    cost = [INF]*nodeNum
    cost[start] = 0
    hq = [(0,start)]
    heapq.heapify(hq)
    while hq:
        hc, hv = heapq.heappop(hq)
        for to, c in adjList[hv]:
            if hc + c >= cost[to]:
                continue
            cost[to] = hc + c
            heapq.heappush(hq, (cost[to],to))
    return cost

# main
N,M,T = map(int,input().split())
A = list(map(int,input().split()))
adj1 = [[] for _ in range(N)]
adj2 = [[] for _ in range(N)]
for i in range(M):
    a,b,c = map(int,input().split())
    adj1[a-1].append((b-1,c))
    adj2[b-1].append((a-1,c))

cost1 = dijkstra(N,0,adj1)
cost2 = dijkstra(N,0,adj2)

ans = 0
for i in range(N):
    ans = max(ans, A[i]*(T-cost1[i]-cost2[i]))

print(ans)