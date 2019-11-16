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
