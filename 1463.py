#baekjoon 1463 1로 만들기 python3


from collections import deque

n = int(input())

queue = deque()
queue.append((n,0))
value = 0
while queue:
  v = queue.popleft()
  if v[0] != 1:
    if v[0] % 3 == 0:
      queue.append((v[0]//3,v[1]+1))
    if v[0] % 2 == 0:
      queue.append((v[0]//2, v[1]+1))
    queue.append((v[0]-1, v[1]+1))
  else:
    value = v[1]
    break

print(value)