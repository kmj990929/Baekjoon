#baekjoon 2475 검증수 python3

numbers = list(map(int, input().split()))

answer = 0
for number in numbers:
  answer += number**2

print(answer%10)