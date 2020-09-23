#baekjoon 2667 단지 번호 붙이기 python3


n = int(input())

def dfs(field, v, visited):
  x,y = v
  visited[y][x] = True

  move = [(-1,0),(1,0),(0,1),(0,-1)]

  count = 1
  for i in move:
    dx = x + i[0]
    dy = y + i[1]
    if(dx >= 0 and dy >= 0 and dx < len(field[0]) and dy < len(field)):
      if(not visited[dy][dx] and field[dy][dx] == 1):
        count += dfs(field, (dx,dy), visited)
  return count

field_map = [[0]*n for _ in range(n)]
visited = [[False]*n for _ in range(n)]

#field 설정
for i in range(n):
  house_ox = input()
  for j in range(n):
    if(int(house_ox[j]) == 1):
      field_map[i][j] = 1

lst = []
for y in range(n):
  for x in range(n):
    if(not visited[y][x] and field_map[y][x] == 1):
      lst.append(dfs(field_map, (x,y), visited))

print(len(lst))
for a in sorted(lst):
  print(a)
