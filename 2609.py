#baekjoon 2609 최대공약수와 최소공배수 python3

a,b = map(int, input().split())

_a, _b = a,b
while _b > 0:
  _a,_b = _b, _a%_b
gcd = _a
print(gcd)
print(a*b//gcd)
