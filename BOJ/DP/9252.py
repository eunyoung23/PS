import sys

input=sys.stdin.readline

str1=input().rstrip()
str2=input().rstrip()
result=[]

len1=len(str1)
len2=len(str2)
data=[[0 for _ in range(len2+1)]for _ in range(len1+1)]

for i in range(1,len1+1):
    for j in range(1,len2+1):
        if str1[i-1]==str2[j-1]:
            data[i][j]=data[i-1][j-1]+1
        else:
            data[i][j]=max(data[i][j-1],data[i-1][j])

print(data[len1][len2])
