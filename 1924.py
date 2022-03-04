#baekjoon 1924 2007년 python3

x,y = map(int, input().split())

month = [31,28,31,30,31,30,31,31,30,31,30,31]
week = ["SUN","MON","TUE","WED","THU","FRI","SAT"]

print(week[(y+sum(month[:x-1]))%7])