# 풀이1
N,M,K = map(int,input().split())
data = list(map(int,input().split()))
data.sort(reverse=True) # data 원본이 역순으로 배열되도록 정렬
sum = 0

while True:
  for i in range(K):
    if M == 0:
      break
    sum += data[0]
    M-=1
  if M == 0:
    break
  sum+=data[1]
  M-=1

print(sum)

# 풀이2
N,M,K = map(int,input().split())
data = list(map(int,input().split()))
data.sort(reverse=True)
sum=0

#가장 큰 수가 더해지는 횟수 계산
count = int(M/(K+1))*K
count += M % (K+1)
sum += count*data[0] # 가장 큰 수 더하기
sum += (M-count)*data[1] # 두번째로 큰 수 더하기

print(sum)
