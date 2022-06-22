import sys
input=sys.stdin.readline

str1=input().rstrip()
str2=input().rstrip()

len1=len(str1)
len2=len(str2)
cache=[[0]*(len2+1)for _ in range(len1+1)]

for i in range(1,len1+1):
    for j in range(1,len2+1):
        if str1[i-1]==str2[j-1]:
            cache[i][j]=cache[i-1][j-1]+1
        else:
            cache[i][j]=max(cache[i][j-1],cache[i-1][j])

print(cache[-1][-1])
