#baekjoon 2230 수 고르기 python3

n,m = map(int, input().split())

numbers = [int(input()) for _ in range(n)]
numbers.sort()

start = 0
end = 0
result = int(1e10)

while True:
  tmp = numbers[end] - numbers[start]
  if tmp < m:
    end += 1
    if end >= n:
      break
  elif tmp == m:
    result = m
    break
  else:
    if tmp < result:
      result = tmp
    start += 1

print(result)
  