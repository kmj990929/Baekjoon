#baekjoon 1806 부분합 python3
     
n,s= map(int,input().split())
numbers = list(map(int, input().split()))

tmpsum = numbers[0]
cnt = 1
start = 0
end = 0
result = len(numbers)+1

while True:
  if tmpsum >= s:
    if result > cnt:
      result = cnt
    tmpsum -= numbers[start]
    start += 1
    cnt -= 1

  else:
    end += 1
    if end >= n:
      break
    tmpsum += numbers[end]
    cnt += 1

if result > len(numbers):
  print(0)
else:
  print(result)
    
    