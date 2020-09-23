#baekjoon 11724 연결요소의 개수 python3

import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())

field = [[] for _ in range(n+1)]
visited = [[False] for _ in range(n+1)]

for i in range(m):
  a,b = map(int, sys.stdin.readline().split())
  field[a].append(b)
  field[b].append(a)

def dfs(field,v,visited):
  visited[v][0] = True
  for i in field[v]:
    if not visited[i][0]:
      dfs(field,i,visited)

count = 0
for a in range(1,n+1):
  if not visited[a][0]:
    dfs(field,a,visited)
    count += 1
print(count)