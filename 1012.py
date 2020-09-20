#baekjoon 1012 유기농 배추 python3

import sys
sys.setrecursionlimit(50000) #이거 안 쓰면 런타임 에러 남

def dfs(field,v,visited):
  x,y = v
  visited[y][x] = True
  move = [(-1,0),(1,0),(0,1),(0,-1)]
  for i in move:
    dx = x + i[0]
    dy = y + i[1]
    if (dx >= 0 and dy >= 0 and dx < len(field_map[0]) and dy < len(field_map)):
      if(not visited[dy][dx] and field_map[dy][dx] == 1):
        dfs(field_map,(dx,dy),visited)

n = int(input())

for _ in range(n):
  m,n,k = map(int,input().split())

  field_map = [[0]*m for i in range(n)]
  visited = [[False]*m for j in range(n)]
  for i in range(k):
    x,y = map(int, input().split())
    field_map[y][x] = 1

  count = 0
  for y in range(n):
    for x in range(m):
      if(not visited[y][x] and field_map[y][x] == 1):
        dfs(field_map, (x,y), visited)
        count += 1
  
  print(count)




