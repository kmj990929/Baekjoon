#baekjoon 11399 ATM python3

n = int(input())
p = list(map(int,input().split()))

p.sort()

tot_time = 0
for i in range(len(p)):
  tot_time += sum(p[:i+1])

print(tot_time)