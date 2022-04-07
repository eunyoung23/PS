arr=[]
posAx=0
posAy=0 
posBx=0  
posBy=0
flag=1

for _ in range(8):
  arr.append(list(map(int,input().split())))
  
for i in range(8):
  for j in range(8):
    if arr[i][j]==1:
      posAx=i
      posAy=j 
    if arr[i][j]==2:
      posBx=i
      posBy=j

if posAx>posBx:
  posAx,posBx=posBx,posAx
if posAy>posBy:
  posAy,posBy=posBy,posAy

if posAx==posBx:
  for i in range(posAy+1,posBy):
    if arr[posAx][i]==3:
      flag=0
      break
    else:
      flag=1

if posAy==posBy:
  for i in range(posAx+1,posBx):
    if arr[i][posAy]==3:
      flag=0
      break
    else:
      flag=1
    
if posAx!=posBx and posAy!=posBy:
  flag=0
  
if flag==1:
  print("1")
else:
  print("0")
