#baekjoon 1987 알파벳 python3

from collections import deque
import sys

input = sys.stdin.readline

r,c = map(int, input().split())
alphabet = [list(input()) for _ in range(r)]

cnt = 1
cursor = (0,0,alphabet[0][0])
moves = [(0,1), (1,0), (0,-1), (-1,0)]

queue = deque([cursor])

while queue:
  now = queue.pop()
  notes = now[2]
  if len(notes) > cnt:
    cnt = len(notes)
  for mm in moves:
    next_y, next_x = now[0]+mm[0], now[1]+mm[1]
    if next_y >=0 and next_y <r and next_x >=0 and next_x < c:
      if alphabet[next_y][next_x] not in notes:
        queue.append((next_y, next_x, notes+alphabet[next_y][next_x]))

print(cnt)  
