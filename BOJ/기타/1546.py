N = int(input())
score = list(map(int,input().split()))
maxValue = max(score)
length = len(score)
sum=0

for i in range(N):
    score[i] = score[i]/maxValue*100

for j in range(N):
    sum+=score[j]

print(sum/length)
