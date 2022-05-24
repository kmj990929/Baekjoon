#baekjoon 5582 공통 부분 문자열 python3

s1 = input()
s2 = input()

length = [[0]*len(s1) for _ in range(len(s2))]

result = 0
for i, a in enumerate(s1):
  for j, b in enumerate(s2):
    if a==b:
      if i==0 or j==0:
        length[j][i] = 1
        if result == 0:
          result = 1
      else:
        length[j][i] = length[j-1][i-1] +1
        result = max(result, length[j][i])

print(result)