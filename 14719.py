#baekjoon 14719 빗물 python3


h,w = map(int, input().split())

field = list(map(int, input().split()))

count = 0
for i in range(1,w-1):
  current = field[i]
  left = max(field[:i])
  right = max(field[i+1:])
  wall = min(left,right)
  if (wall - current > 0):
    count += wall-current

print(count)