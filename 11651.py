#baekjoon 11651 좌표 정렬하기 2 python3

n = int(input())
coordinate = dict()

for _ in range(n):
  x,y = map(int, input().split())
  if y in coordinate:
    coordinate[y].append(x)
  else:
    coordinate[y] = [x]

for y in sorted(coordinate.keys()):
  for point in sorted(coordinate[y]):
    print(point, y)