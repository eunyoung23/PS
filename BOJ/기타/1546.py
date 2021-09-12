N = int(input())
score = list(map(int,input().split()))
maxValue = max(score)

for i in range(N):
    score[i] = score[i]/maxValue*100

print(sum(score)/N)
