#baekjoon 1966 프린터 큐 python3

from collections import deque

num = int(input())

for i in range(num):
  n, m = map(int, input().split())
  queue = deque(map(int, input().split()))
  idx = m
  count = 1
  while len(queue) > 0:
    if(queue[0] < max(queue)):
      if (idx == 0):
        idx = len(queue)-1
      else:
        idx -= 1 
      queue.append(queue.popleft())
    else:
      if (idx == 0):
        print(count)
        break
      else:
        queue.popleft()
        count += 1
        idx -= 1
