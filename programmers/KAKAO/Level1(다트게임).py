#35분
#1-dartResult를 문자로 이루어진 배열로 만든다.
#2-하나씩 반복문을 돌린다.
#3-인덱스를 이용해서 반복문에서 처리해준다 -> *과 #인 경우도 dart[-2]*2 이런식으로 처리하기
#4-answer연산값을 어떻게 구해야하지? - stack 자료구조를 이용해야 하나?
#5-stack 자료구조에서 값을 빼서 answer값으로 구해줌.

#******10인경우 예외처리해서 처리하기!!
def solution(dartResult):
    answer = 0
    stack=[] 
    
    dartResult=dartResult.replace(str(10),'A')
    
    for i in range(len(dartResult)):
        if dartResult[i]=='S':
            stack.append(stack.pop(-1))
        elif dartResult[i]=='D':
            num=stack.pop(-1)
            stack.append(num*num)
        elif dartResult[i]=='T':
            num=stack.pop(-1)
            stack.append(num*num*num)
        elif dartResult[i]=="*":
            if len(stack)>=2:
                num1=stack.pop(-1)
                num2=stack.pop(-1)
                stack.append(num2*2)
                stack.append(num1*2)
            if len(stack)==1:
                stack.append(stack.pop(-1)*2)
        elif dartResult[i]=="#":
            stack.append(-1*(stack.pop(-1))) 
        elif dartResult[i]=="A":
            stack.append(10)
        else:
            stack.append(int(dartResult[i]))
            
    for i in range(len(stack)):
        answer+=stack[i]
    
    return answer
