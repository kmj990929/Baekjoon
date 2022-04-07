#baekjoon 2473 세 용액 python3

n = int(input())
solutions = list(map(int, input().split()))
solutions.sort()

minimum = 10**10
for mid in range(1,n):
  left = 0
  right = n-1
  while left < right:
    if left==mid or right==mid:
      break
    tmp = solutions[left]+solutions[mid]+solutions[right]
    if abs(tmp) < minimum:
      minimum = abs(tmp)
      target = (solutions[left], solutions[mid], solutions[right])
    if tmp > 0:
      right -=1
    elif tmp < 0 :
      left += 1
    else:
      break

print(" ".join(map(str,target)))
