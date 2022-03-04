#baekjoon 1149 RGB거리 python3

from collections import deque

n = int(input())
field = []

for _ in range(n):
    field.append(list(map(int,input().split())))

last_cost = field[0]


def calculate_minimum_cost(cursor, last_cost):
    cost = []
    for i in range(3):
        candidates = []
        for j in range(3):
            if i == j:
                continue
            else:
                candidates.append(cursor[i] + last_cost[j])
        cost.append(min(candidates))
        candidates = []   
    return cost

for i in range(1,n):
    ith = field[i]
    last_cost = calculate_minimum_cost(ith, last_cost)

print(min(last_cost))
