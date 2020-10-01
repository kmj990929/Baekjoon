#baekjoon 4963 섬의 개수 python3

from collections import deque
import sys

sys.setrecursionlimit(100000)

def dfs(graph, visited, v):
  global w,h
  x,y = v
  visited[y][x] = True
  move = [(-1,0),(1,0),(0,1),(0,-1),(-1,-1),(1,1),(-1,1),(1,-1)]
  for i in move:
    dx = x + i[0]
    dy = y + i[1]
    if ((0<=dx<w) and (0<= dy < h)):
      if (graph[dy][dx] == 1 and not visited[dy][dx]):
        dfs(graph, visited, (dx,dy))

w,h = map(int, input().split())
while(w!=0 and h!= 0):
  #field 설정
  field = []
  for i in range(h):
    map_row = list(map(int,sys.stdin.readline().split()))
    field.append(map_row)
  visited = [[False]*w for _ in range(h)]  

  count = 0
  for j in range(h):
    for i in range(w):
      if (field[j][i] ==1 and not visited[j][i]):
        count += 1
        dfs(field,visited, (i,j))

  print(count)
  
  
  w,h = map(int,sys.stdin.readline().split())
