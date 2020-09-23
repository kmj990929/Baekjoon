#baekjoon 7576 토마토 python3


from collections import deque
import sys

m, n = map(int, input().split())

field = []
queue = deque()

#field 설정
for i in range(n):
  field_row = list(map(int, sys.stdin.readline().split()))
  for j in range(m):
    if (field_row[j] == 1):
      queue.append((j,i))
  field.append(field_row)

def bfs(m,n,box,queue):
  move = [(-1,0),(1,0),(0,1),(0,-1)]
  day = -1
  while queue:
    day += 1
    for j in range(len(queue)):
      v = queue.popleft()
      x,y = v
      for i in move:
        dx = x + i[0]
        dy = y + i[1]
        if (dx >= 0 and dy >= 0 and dx < m and dy < n and box[dy][dx] == 0):
          box[dy][dx] = 1
          queue.append((dx,dy))
  
  for z in box:
    if 0 in z:
      return -1
  return day

print(bfs(m,n,field,queue))

