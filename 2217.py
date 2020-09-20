#baekjoon 2217 로프 python3


n = int(input())

rope_types = []
for i in range(n):
  rope_types.append(int(input()))

rope_types.sort()

weight = []
for j in range(n):
  w = rope_types[j]*(n-j)
  weight.append(w)

print(max(weight))