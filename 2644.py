#baekjoon 2644 촌수계산 python3

from collections import deque
import sys

n = int(input())
a,b = map(int, input().split())
m = int(input())

#graph 설정
graph = [[] for _ in range(n+1)]
for i in range(m):
  x,y = map(int, sys.stdin.readline().split())
  graph[x].append(y)
  graph[y].append(x)

queue = deque([a])
visited = [False]*(n+1)

def bfs(graph, queue, b):
  check = 0
  while queue:
    check += 1
    for j in range(len(queue)):
      v = queue.popleft()
      visited[v] = True
      for i in graph[v]:
        if (i == b):
          return check
        elif (not visited[i]):
          queue.append(i)
  return -1

print(bfs(graph, queue, b))

