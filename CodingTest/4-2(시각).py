# 풀이
N =int(input())
count=0

for i in range(0,N+1):
  for j in range(0,60):
    for z in range(0,60):
      if '3' in str(i)+str(j)+str(z):
        count+=1

print(count)
