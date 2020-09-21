#baekjoon 1260 dfs와 bfs python3

import sys
from collections import deque

n,m,v = map(int, input().split())

#field 설정
field = [[] for _ in range(n+1)]
for i in range(m):
  a,b = map(int, sys.stdin.readline().split())
  field[a].append(b)
  field[b].append(a)

for j in range(1,n+1):
  field[j].sort()

visited_dfs = [False] * (n+1)
visited_bfs = [False] * (n+1)

def dfs(field,v,visited):
  visited[v] = True
  print(v, end = " ")
  for i in field[v]:
    if not visited[i]:
      dfs(field,i,visited)


def bfs(field,start,visited):
  queue = deque([start])
  visited[start] = True
  while queue:
    v = queue.popleft()
    print(v, end = " ")
    for i in field[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

dfs(field,v,visited_dfs)
print()
bfs(field,v,visited_bfs)