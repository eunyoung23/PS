N = list(input())
result=0
stack =[]

for i in range(len(N)):
    if N[i]=="(":
        stack.append("(")
    else:
        if N[i-1]=="(":
            stack.pop()
            result+=len(stack)
        else:
            stack.pop()
            result+=1

print(result)
