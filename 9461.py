#baekjoon 9461 파도반 수열 python3

t = int(input())
_input = [int(input()) for _ in range(t)]

triangle = {1:1,2:1,3:1,4:2,5:2}
for i in _input:
  for j in range(6,i+1):
    if not j in triangle:
      triangle[j] = triangle[j-1]+triangle[j-5]
  print(triangle[i])
  