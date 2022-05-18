#baekjoon 2003 수들의 합 2 python3

n,m=map(int, input().split())
numbers = list(map(int, input().split()))

start = 0 
end = 0
tmpsum = numbers[0]
cnt = 0

while True:
  if tmpsum < m:
    end += 1
    if end >= n:
      break
    tmpsum += numbers[end]
  elif tmpsum == m:
    cnt += 1
    tmpsum -= numbers[start]
    start += 1
  else:
    tmpsum -= numbers[start]
    start += 1

print(cnt)
    
