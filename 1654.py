#baekjoon 1654 랜선 자르기 python3

k,n = map(int, input().split())
lines = []
for _ in range(k):
  lines.append(int(input()))

start, end = 1, max(lines)
while start <= end:
  mid = (start+end)//2

  tmp = 0
  for line in lines:
    tmp += line//mid

  if tmp >= n:
    start = mid+1
  else:
    end = mid-1

print(end)