#baekjoon 10026 적록색약 python3
#bfs 잘못 구현했는데??ㅠㅠ


import sys
from collections import deque

n = int(input())

field = [[0]*n for _ in range(n)]
field2 = [[0]*n for _ in range(n)]
visited = [[False]*n for _ in range(n)]
visited2 = [[False]*n for _ in range(n)]

for i in range(n):
  field_row = sys.stdin.readline().rstrip()
  for j in range(n):
    if field_row[j] == "R":
      field[i][j] = 1
      field2[i][j] = 1
    elif field_row[j] == "G":
      field[i][j] = 2
      field2[i][j] = 1
    elif field_row[j] == "B":
      field[i][j] = 3
      field2[i][j] = 3

def bfs(field,start,visited,color):
  queue = deque([start])
  x,y = start
  visited[y][x] = True
  move = [(-1,0),(1,0),(0,1),(0,-1)]
  while queue:
    vx,vy = queue.popleft()
    for i in move:
      dx = vx + i[0]
      dy = vy + i[1]
      if (dx >= 0 and dy >= 0 and dx < n and dy < n):
        if(field[dy][dx] == color and not visited[dy][dx]):
          bfs(field,(dx,dy),visited,color)

count = 0
for x in range(n):
  for y in range(n):
      if(visited[y][x] == False):
        color = field[y][x]
        bfs(field,(x,y),visited,color)
        count += 1

count2 = 0
for x in range(n):
  for y in range(n):
      if(visited2[y][x] == False):
        color2 = field2[y][x]
        bfs(field2,(x,y),visited2,color2)
        count2 += 1

print(count,count2)