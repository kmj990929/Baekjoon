#baekjoon 2805 나무 자르기 python3

n, m = map(int, input().split())

trees = list(map(int, input().split()))

start, end = 0, max(trees)

while start <= end:
  mid = (start+end)//2

  tmp = 0
  for i in trees:
    if i > mid:
      tmp += i-mid

  if tmp >= m:
    start = mid+1
  else:
    end = mid-1

print(end)