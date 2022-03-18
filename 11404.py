#baekjoon 11404 플로이드 python3
import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())
graph = [[INF]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
  graph[i][i] = 0
  
for _ in range(m):
  a,b,c = map(int, input().split())
  if graph[a][b] < c:
    continue
  graph[a][b] = c

for k in range(1,n+1):
  for a in range(1,n+1):
    for b in range(1,n+1):
      graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

for a in range(1,n+1):
  answer = ""
  for b in range(1,n+1):
    if graph[a][b] == INF:
      answer += "0 "
    else:
      answer += str(graph[a][b]) + " "
  print(answer.strip())