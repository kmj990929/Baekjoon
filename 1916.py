#baekjoon 1916 최소비용 구하기 python3
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())
graph = [[] for i in range(n+1)]
for _ in range(m):
  a,b,c = map(int, input().split())
  graph[a].append((b,c))

start, end = map(int, input().split())

def dijkstra(start):
  q = []
  distance = [INF]*(n+1)
  heapq.heappush(q, (0,start))
  distance[start] = 0
  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    for i in graph[now]:
      next_node = i[0]
      weight = i[1]
      cost = dist+weight
      if cost < distance[next_node]:
        distance[next_node] = cost
        heapq.heappush(q, (cost, next_node))
  return distance

print(dijkstra(start)[end])
  