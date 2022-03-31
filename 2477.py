#baekjoon 2477 참외밭 python3

k = int(input())
max_x, max_y = 0, 0
max_x_idx, max_y_idx = 0,0
length = []
for i in range(6):
  _, l = map(int,input().split())
  if i % 2 == 0:
    if max_x<l:
      max_x = l
      max_x_idx = i
  else:
    if max_y<l:
      max_y = l
      max_y_idx = i
  length.append(l)

tmp = max(max_x_idx, max_y_idx)
if tmp == len(length)-1 and min(max_x_idx, max_y_idx)==0:
  tmp = 0

small_x_idx = (tmp+2)%len(length)
small_y_idx = (small_x_idx+1)%len(length)

area = max_x*max_y-length[small_x_idx]*length[small_y_idx]
print(area*k)