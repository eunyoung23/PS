# 내 풀이
def solution(board, moves):
    answer = 0
    stack=[]
    
    for num in moves:
        for line in board:
            if line[num-1] == 0:
                continue
            else:
                stack.append(line[num-1])
                if len(stack) >=2:
                    if stack[-1] == stack[-2]:
                        stack.pop(-1)
                        stack.pop(-1)
                        answer+=2
                line[num-1]=0
                break
    
    return answer
