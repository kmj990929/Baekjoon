#baekjoon 1932 정수 삼각형 python3

n = int(input())

triangle = []
for i in range(1,n+1):
    line = list(map(int, input().split()))
    triangle.append(line)

score = triangle[0]

def down(layer, score):
    next_scores = []
    for i in range(len(layer)):
        if i == 0:
            next_scores.append(score[i] + layer[i]) 
        elif i == len(score):
            next_scores.append(score[i-1] + layer[i])
        else:
            next_score = max(score[i-1] + layer[i], score[i] + layer[i])
            next_scores.append(next_score)
    return next_scores

for i in range(n-1):
    layer = triangle[i+1]
    score = down(layer, score)

print(max(score))
