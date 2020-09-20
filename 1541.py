#baekjoon 1541 잃어버린 괄호 python3


sen = input()
sen = sen.split('-')

for i in range(len(sen)):
  if(sen[i].find('+') != -1):
    sum_list = list(map(int,sen[i].split('+')))
    sen[i] = sum(sum_list)
  else:
    sen[i] = int(sen[i])

result = sen[0]
for j in range(1,len(sen)):
  result -= sen[j]

print(result)