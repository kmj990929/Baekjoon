#baekjoon 1920 수 찾기 python3

n = int(input())
numbers = list(map(int, input().split()))
m = int(input())
find_numbers = list(map(int, input().split()))

numbers.sort()

for nn in find_numbers:
  start, end = 0, len(numbers)-1
  while start <= end:
    mid = (end+start)//2
    if nn == numbers[mid]:
      print(1)
      break
    elif nn > numbers[mid]:
      start = mid+1
    elif nn < numbers[mid]:
      end = mid-1
  else:
    print(0)
    
