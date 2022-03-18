#baekjoon 9465 스티커 python3

t = int(input())

for _ in range(t):
  n = int(input())
  sticker = [list(map(int, input().split())) for _ in range(2)]
  score1 = [sticker[0][0]]
  score2 = [sticker[1][0]]
  score0 = [0]

  for i in range(1,n):
    pre_score1, pre_score2, pre_score0 = score1[-1], score2[-1], score0[-1]
    score1.append(max(pre_score2,pre_score0)+sticker[0][i])
    score2.append(max(pre_score1,pre_score0)+sticker[1][i])
    score0.append(max(pre_score2,pre_score1))

  print(max(score0[-1],score1[-1],score2[-1]))