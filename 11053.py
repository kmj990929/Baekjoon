#baekjoon 11053 가장 긴 증가하는 부분 수열 python3

n = int(input())
numbers = list(map(int, input().split()))

dp = [1]

for i, number in enumerate(numbers[1:], start=1):
  length_set = [length for nn, length in zip(numbers[:i],dp[:i]) if nn<number]
  if length_set:
    dp.append(max(length_set)+1)
  else:
    dp.append(1)

print(max(dp))
      
  