#baekjoon 2467 용액 python3

n = int(input())
solutions = list(map(int, input().split()))

minimum = 10**10
left = 0
right = n-1
while left < right:
  tmp = solutions[left] + solutions[right]
  if abs(tmp) < minimum:
    minimum = abs(tmp)
    target = (solutions[left], solutions[right])
  if tmp > 0:
    right -= 1
  elif tmp < 0:
    left += 1
  else: # tmp = 0
    break

print(" ".join(map(str,target)))