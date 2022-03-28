#baekjoon 11050 이항 계수 1 python3

n,k = map(int, input().split())

factorial = [1]

for i in range(1,n+1):
  factorial.append(factorial[i-1]*i)

print(int(factorial[n]/(factorial[n-k]*factorial[k])))