#baekjoon 10816 숫자 카드 2 python3

n = int(input())
numbers = list(map(int, input().split()))

tmp = dict()
for number in numbers:
  if number in tmp:
    tmp[number] += 1
  else:
    tmp[number] = 1

m = int(input())
test = list(map(int, input().split()))

answer = ""
for t in test:
  if t in tmp:
    answer += str(tmp[t]) + " "
  else:
    answer += "0 "
print(answer.strip())