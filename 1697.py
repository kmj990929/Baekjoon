#baekjoon 1697 숨바꼭질 python3

from collections import deque

n,k = map(int, input().split())
dp_table = {n:0}
queue = deque()
queue.append(n)

while queue:
  cursor = queue.popleft()
  if cursor < 0:
    continue
  if cursor-1 not in dp_table:
    dp_table[cursor-1] = dp_table[cursor]+1
    queue.append(cursor-1)
  if cursor+1 not in dp_table:
    dp_table[cursor+1] = dp_table[cursor]+1
    queue.append(cursor+1)
  if cursor*2 not in dp_table and cursor*2 <=100000:
    dp_table[cursor*2] = dp_table[cursor]+1
    queue.append(cursor*2)

  if k in dp_table:
    print(dp_table[k])
    break