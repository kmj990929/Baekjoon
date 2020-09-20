#baekjoon 1158 요세푸스 문제 python3

from collections import deque

n,k = map(int, input().split())

queue = deque()

for i in range(1,n+1):
  queue.append(i)

result = []
while len(queue) > 0:
  for i in range(k-1):
    queue.append(queue.popleft())
  result.append(queue.popleft())

print('<',end = "")
for i in range(n-1):
  print(f'{result[i]}, ', end= '')
print(f'{result[n-1]}>')
