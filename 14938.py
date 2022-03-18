#baekjoon 14938 서강그라운드 python3

import sys
input = sys.stdin.readline
INF = int(1e9)

n,m,r = map(int, input().split())
items = list(map(int, input().split()))

graph=[[INF]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
  graph[i][i] = 0

for _ in range(r):
  a,b,c = map(int, input().split())
  graph[a][b] = c
  graph[b][a] = c

for k in range(1,n+1):
  for a in range(1,n+1):
    for b in range(1,n+1):
      graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

available_item = 0
for x in range(1,n+1):
  totitem = 0
  for y in range(1,n+1):
    if graph[x][y] <=m:
      totitem+= items[y-1]
  if totitem > available_item:
    available_item = totitem

print(available_item)