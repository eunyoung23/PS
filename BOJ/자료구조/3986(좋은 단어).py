import sys

input=sys.stdin.readline

N=int(input())

words=[]

result=0

for _ in range(N):
    words.append(input().strip())

for word in words:
    stack=[]
    stack.append(word[0])
    for i in range(1,len(word)):
        if len(stack)==0:
            stack.append(word[i])
        elif stack[-1]==word[i]:
            stack.pop(-1)
        else:
            stack.append(word[i])
    if len(stack)==0:
        result+=1
    else:
        pass

print(result)
