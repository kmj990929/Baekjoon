#baekjoon 4153 직각삼각형 python3


while 1:
  a,b,c = map(int, input().split())

  if (a == 0 and b == 0 and c == 0):
    break

  t = max(a,b,c)

  result = 0
  for i in [a,b,c]:
    if (i != t):
      result += i**2

  if (t**2 == result):
    print("right")
  else:
    print("wrong")