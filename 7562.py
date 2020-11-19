#baekjoon 7562 나이트의 이동 python3

from collections import deque

test_num = int(input())

for _ in range(test_num):
  n = int(input())

  move = [(2,1),(2,-1),(-2,1),(-2,-1),(-1,2),(1,2),(-1,-2),(1,-2)]

  sx, sy = map(int, input().split())
  fx, fy = map(int, input().split())

  sx += 1
  sy += 1
  fx += 1
  fy += 1

  visited = [[False]*n for _ in range(n)]

  queue = deque()
  queue.append((sx,sy))
  visited[sy-1][sx-1] = True

  distance = 0
  flag = 0
  while queue:
      for _ in range(len(queue)):
          v = queue.popleft()
          sx,sy = v
          if (v==(fx,fy)):
              flag = 1
              break
          for m in move:
              dx = sx + m[0]
              dy = sy + m[1]
              if (dx >= 1 and dy >= 1 and dx <= n and dy <= n and visited[dy-1][dx-1] == False):
                  queue.append((dx,dy))
                  visited[dy-1][dx-1] = True
      if flag ==1:
          print(distance)
          break
      distance += 1

        
    
    
