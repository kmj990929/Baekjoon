#baekjoon 1092 배 python3

n = int(input())
cranes = list(map(int, input().split()))
m = int(input())
boxes = list(map(int, input().split()))
cranes.sort(reverse=True)
boxes.sort(reverse=True)

if cranes[0] < boxes[0]:
  print(-1)
else:
  time = 0
  while boxes:
    time += 1
    for crane in cranes:
      for i in range(len(boxes)):
        if crane >= boxes[i]:
          boxes.pop(i)
          break
  
  print(time)
