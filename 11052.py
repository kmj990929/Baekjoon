#baekjoon 11052 카드 구매하기 python3

n = int(input())
cards = list(map(int, input().split()))
cards = [0] + cards

for num, price in enumerate(cards[1:], start=1):
  for i in range(num//2+1):
    cards[num] = max(cards[num], cards[num-i]+cards[i])

print(cards[n])
    