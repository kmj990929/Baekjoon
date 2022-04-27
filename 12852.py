#baekjoon 12852 1로 만들기 2 python3

from collections import defaultdict

n = int(input())

checked = [n]
lst = defaultdict(list)
lst[n].append(n)
finished = False

while True:
  tmp = []
  for t in checked:
    if t%3==0 and t//3 not in lst:
      lst[t//3] = lst[t] + [t//3]
      tmp.append(t//3)
    if t%2==0 and t//2 not in lst:
      lst[t//2] = lst[t] + [t//2]
      tmp.append(t//2)
    if t-1 not in lst:
      lst[t-1] = lst[t] + [t-1]
      tmp.append(t-1)

    if 1 in lst:
      finished = True
      break

  if finished:
    break
  checked = tmp

print(len(lst[1])-1)
print(" ".join(map(str,lst[1])))