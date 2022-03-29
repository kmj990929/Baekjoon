#baekjoon 11866 요세푸스 문제 0 python3

from collections import deque

n,k = map(int, input().split())
queue = deque(list(range(1,n+1)))

result = []

for _ in range(n):
  queue.rotate(-k+1)
  result.append(queue.popleft())

print("<"+", ".join(map(str,result))+">")