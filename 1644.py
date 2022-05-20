#baekjoon 1644 소수의 연속합 python3

n = int(input())

# 소수 구하기
primes = []
check = [False,False] + [True]*(n-1)

for i in range(2, n+1):
  if check[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
      check[j] = False


# 가능한 연속합 구하기
if primes:
  start = 0
  end = 0
  tmpsum = primes[0]
  cnt = 0
  
  while True:
    if tmpsum == n:
      cnt += 1
      tmpsum -= primes[start]
      start += 1
  
    elif tmpsum > n:
      tmpsum -= primes[start]
      start += 1
  
    else:
      end += 1
      if end >= len(primes):
        break
      tmpsum += primes[end]
  
  print(cnt)
else:
  print(0)
