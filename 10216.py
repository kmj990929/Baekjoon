#baekjoon 10216 Count Circle Groups python3

import sys
input = sys.stdin.readline

t = int(input())

def calcul_dist(p1, p2):
  p1x, p1y = p1[0], p1[1]
  p2x, p2y = p2[0], p2[1]
  return (p1x-p2x)**2+(p1y-p2y)**2
  
def check_map():
  n = int(input())
  points = []
  _map = [[] for _ in range(n)]
  for tmp in range(n):
    x,y,r = map(int, input().split())
    length = len(points)
    for i in range(length):
      before = points[i]
      distance = calcul_dist((before[0], before[1]), (x,y))
      if distance <= r+before[2]:
        _map[i].append(tmp)
        _map[tmp].append(i)
    points.append((x,y,r))
  return _map

def find_group(start):
  visited[start] = True
  for neighbor in range(n):
    if neighbor == start:
      continue

    if not visited[neighbor] and calcul_dist(_map[start], _map[neighbor]) <= (_map[start][2]+_map[neighbor][2])**2:
      find_group(neighbor)
  
for _ in range(t):
  n = int(input())
  _map = []
  for _ in range(n):
    _map.append(list(map(int, input().split())))

  visited = [False]*n
  cnt = 0
  for i in range(n):
    if not visited[i]:
      cnt += 1
      find_group(i)

  print(cnt)
  
