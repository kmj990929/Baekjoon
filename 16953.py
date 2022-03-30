#baekjoon 16953 A -> B python3

from collections import deque

a,b = map(int, input().split())

queue = deque([(a,0)])
while queue:
  now = queue.popleft()
  num, cnt = now[0], now[1]
  if num == b:
    print(cnt+1)
    break
  if num > b:
    continue
  queue.append((num*2,cnt+1))
  queue.append((int(str(num)+"1"), cnt+1))
else:
  print(-1)
    