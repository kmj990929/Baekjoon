#baekjoon 1504 특정한 최단 경로 python3
import heapq
import sys
input = sys.stdin.readline
INF = float('inf')

n,e = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(e):
  a,b,c = map(int, input().split())
  graph[a].append((b,c))
  graph[b].append((a,c))
v1,v2 = map(int, input().split())

def dijkstra(start):
  q = []
  distance = [INF]*(n+1)
  heapq.heappush(q,(0,start))
  distance[start] = 0
  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    for i in graph[now]:
      next_node = i[0]
      weight = i[1]
      cost = dist+i[1]
      if cost < distance[next_node]:
        distance[next_node] = cost
        heapq.heappush(q, (cost, next_node))
  return distance
  
dist_1 = dijkstra(1)
dist_v1 = dijkstra(v1)
dist_v2 = dijkstra(v2)

d_v1v2 = dist_1[v1]+dist_v1[v2]+dist_v2[n]
d_v2v1 = dist_1[v2]+dist_v2[v1]+dist_v1[n]

if d_v1v2 >= INF and d_v2v1 >= INF:
  print(-1)
else:
  print(min(d_v1v2, d_v2v1))
    