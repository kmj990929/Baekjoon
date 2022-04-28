#baekjoon 10819 차이를 최대로 python3

from itertools import permutations

n = int(input())
numbers = list(map(int, input().split()))

maxsum = 0
for candidate in list(permutations(numbers,n)):
  totsum = 0
  for a,b in zip(candidate, candidate[1:]):
    totsum += abs(a-b)

  if totsum > maxsum:
    maxsum = totsum

print(maxsum)