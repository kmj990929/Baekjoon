#baekjoon 2493 탑 python3

n = int(input())
towers = list(map(int, input().split()))

stack = [(0,0)]
answer = []
for i, tower in enumerate(towers,start=1):
  while stack:
    if stack[-1][1] >= tower:
      answer.append(stack[-1][0])
      stack.append((i,tower))
      break
    else:
      stack.pop()
  else:
    answer.append(0)
    stack.append((i,tower))

print(" ".join(map(str, answer)))
    