def solution(s):
    answer =True
    stack=[]
    
    for idx in range(len(s)):
        if len(stack)==0:
            stack.append(s[idx])
        else:
            if stack[-1]=="(":
                if s[idx]=="(":
                    stack.append(s[idx])
                else:
                    stack.pop()
            else:
                stack.append(s[idx])
                    
                    
    if len(stack)!=0:
        answer=False

    return answer