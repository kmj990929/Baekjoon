#baekjoon 2579 계단 오르기 python3

n = int(input())

score = [0]

for _ in range(n):
  score.append(int(input()))

if n==1:
  print(score[1])
elif n ==2:
  print(score[1]+score[2])
else:
  first_step = [0,score[1],score[2]]
  second_step = [0,score[1],score[1]+score[2]]

  for i in range(3,n+1):
    first_step.append(max(second_step[i-2]+score[i], first_step[i-2]+score[i]))
    second_step.append(first_step[i-1]+score[i])

  print(max(first_step[n], second_step[n]))
