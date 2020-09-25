#baekjoon 1085 직사각형에서 탈출 python3

x,y,w,h = map(int, input().split())

mx = w-x
my = h-y

print(min(x,y,mx,my))