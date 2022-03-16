#baekjoon 10815 숫자 카드 python3

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))

cards.sort()

answer = ""
for target in targets:
  start, end = 0, n-1
  while start <= end:
    mid = (start+end)//2
    if target == cards[mid]:
      answer += "1 "
      break
    elif target > cards[mid]:
      start = mid+1
    elif target < cards[mid]:
      end = mid-1
  else:
    answer += "0 "

print(answer.strip())
  