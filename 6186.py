#baekjoon 6186 best grass python3


import sys

sys.setrecursionlimit(100000)

r,c = map(int, input().split())

field = [[0]*c for _ in range(r)]
visited = [[False]*c for _ in range(r)]

#field 입력
for i in range(r):
  input_field = input()
  for j in range(c):
    if(input_field[j] == '#'):
      field[i][j] = 1

move = [(-1,0), (1,0), (0,1), (0,-1)]
def dfs(field, v, visited):
  global r,c
  x,y = v
  visited[y][x] = True
  for i in move:
    dx = x+i[0]
    dy = y+i[1]
    if(dx >= 0 and dy >= 0 and dx < c and dy < r):
      if field[dy][dx] == 1 and not visited[dy][dx]:
        dfs(field, (dx,dy), visited)

count = 0
for y in range(r):
  for x in range(c):
    if(field[y][x] == 1 and not visited[y][x]):
      dfs(field, (x,y), visited)
      count += 1

print(count)