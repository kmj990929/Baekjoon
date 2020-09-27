#baekjoon 2468 안전 영역 python3

import sys
sys.setrecursionlimit(50000)

n = int(input())

def dfs(field, visited, v, margin):
  x,y = v
  visited[y][x] = True
  move = [(0,1),(0,-1),(1,0),(-1,0)]
  for i in move:
    dx = x + i[0]
    dy = y + i[1]
    if (dx >= 0 and dy >= 0 and dx < n and dy < n):
      if (not visited[dy][dx] and field[dy][dx] > margin):
        dfs(field, visited,(dx,dy),margin)

field = []
max_tot = 0

#field 설정
for _ in range(n):
  field_row = list(map(int, input().split()))
  max_row = max(field_row)
  if (max_row > max_tot):
    max_tot = max_row
  field.append(field_row)

num_list = []
for i in range(max_tot):
  num = 0
  visited = [[False]*n for i in range(n)]
  for y in range(n):
    for x in range(n):
      if(field[y][x] > i and not visited[y][x]):
        num += 1
        dfs(field, visited, (x,y),i)
  num_list.append(num)

print(max(num_list))
