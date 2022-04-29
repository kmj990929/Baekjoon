#baekjoon 14889 스타트와 링크 python3
        
from itertools import combinations

n = int(input())
s = []
for _ in range(n):
  s.append(list(map(int,input().split())))
tot = list(range(n))

mindiff = 10**9
for team in list(combinations(tot,n//2)):
  adv = 0
  o_adv = 0
  
  o_team = list(set(tot)-set(team))

  for i in range(n//2):
    for j in range(i+1,n//2):
      adv += s[team[i]][team[j]] + s[team[j]][team[i]]
      o_adv += s[o_team[i]][o_team[j]] + s[o_team[j]][o_team[i]]

  advdiff = abs(adv-o_adv)

  if advdiff < mindiff:
    mindiff = advdiff

print(mindiff)