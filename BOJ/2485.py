N=int(input())
arr=[]
tree=[]
cnt=0

for i in range(N):
  arr.append(int(input()))
  
for i in range(N-1):
  tree.append(arr[i+1]-arr[i])
  
tree.sort()

def gcd(a,b):
  while True:
    temp=a%b 
    if temp==0:
      return b
      break
    a=b 
    b=temp
    
num=gcd(tree[0],tree[1])  

for i in range(1,len(tree)):
  num=gcd(num,tree[i])

for i in range(len(arr)-1):
  cnt+=(arr[i+1]-arr[i])//num-1
  
print(cnt)
