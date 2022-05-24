#baekjoon 1309 동물원 python3

n = int(input())
house = [1]*3

for _ in range(2,n+1):
  new_house = [0]*3

  for i in range(3):
    if i==0:
      new_house[0] += house[i]
      new_house[1] += house[i]
      new_house[2] += house[i]
    elif i==1:
      new_house[0] += house[i]
      new_house[2] += house[i]
    else:
      new_house[0] += house[i]
      new_house[1] += house[i]

  house = new_house
  
print(sum(house)%9901)