T=int(input())

arr=[]
for _ in range(T):
    arr.append(int(input()))

data=[0]*11

data[1]=1
data[2]=2
data[3]=4

for i in range(4,11):
    data[i]=data[i-1]+data[i-2]+data[i-3]


for i in arr:
    print(data[i])
