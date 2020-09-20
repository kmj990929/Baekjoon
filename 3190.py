#baekjoon 3190 뱀 python3

from collections import deque

n = int(input()) # 보드의 크기
k = int(input()) # 사과의 갯수

#맵 만들기
d = [[0] * n for _ in range(n)]

#사과 놓기
for i in range(k):
  x, y = map(int, input().split())
  d[y-1][x-1] = 1

#뱀 만들기
snake = deque()
snake.append((0,0))

#전진하는 경우
def front(dir, x, y):
  if(dir == 0):
    x += 1
  elif(dir == 1):
    y -= 1

  elif(dir == 2):
    x -= 1
  else:
    y += 1
  return (x, y)

#방향 전환
l = int(input())

change = deque()
for i in range(l):
  ch_x, ch_y = input().split()
  ch_x = int(ch_x)
  change.append((ch_x, ch_y))

sec = 0
idx_x = 0
idx_y = 0
length = 1
current_dir = 0

while True:
  sec += 1
  x, y = front(current_dir, idx_x, idx_y)
  #맵에서 벗어날 경우
  if (x < 0 or y < 0 or x >= n or y >= n):
    break
  #몸에 닿을 경우
  elif ((x,y) in snake):
    break
  #사과가 있을 경우
  elif (d[x][y] == 1):
    length += 1
    snake.append((x,y))
    d[x][y] = 0
  #사과 없이 그냥 전진할 경우
  else:
    snake.popleft()
    snake.append((x,y))

  #방향전환
  if(len(change) == 0):
    pass
  else:
    if(change[0][0] == sec):
      if (change[0][1] == "L"):
        current_dir = (current_dir+1) % 4
      elif (change[0][1] == "D"):
        current_dir = (current_dir-1) % 4
      change.popleft()

  idx_x, idx_y = x,y  
  print("-----sec-----",sec)
  print("x y is ",x,y)
  print("snake is ",snake)
  print("dir is ",current_dir) 

print(sec)