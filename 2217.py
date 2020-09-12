#baekjoon 2217 로프 python3


n = int(input())

rope_type = []
for i in range(n):
  rope_type.append(int(input()))

rope_type.sort()

weight = []
for j in range(n):
  w = rope_type[j]*(n-j)
  weight.append(w)

print(max(weight))