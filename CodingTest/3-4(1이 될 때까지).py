# 풀이 1
N,K = map(int,input().split(" "))
count = 0

while N>=K:
  while N%K != 0:
    N-=1
    count+=1
  N=N//K
  count+=1
  
while N>1:
  N-=1
  count+=1

print(count)


# 풀이 2
N,K = map(int,input().split(" "))  # N=25/K=3
count = 0

while True:
  target = (N//K)*K
  count += (N-target)
  N = target
  if N<K:
    break
  count +=1
  N//=K

#마지막으로 남은 수에 대해서 1씩 빼기
count += (N-1)
print(count)
