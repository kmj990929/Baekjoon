#baekjoon 2075 N번째 큰 수 python3

import heapq

n = int(input())
heap = []

for _ in range(n):
  number = list(map(int, input().split()))

  if not heap:
    for num in number:
      heapq.heappush(heap, num)
  else:
    for num in number:
      if heap[0] < num:
        heapq.heappush(heap, num)
        heapq.heappop(heap)

print(heap[0])