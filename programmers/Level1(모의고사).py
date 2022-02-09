# 내 풀이
def solution(answers):
    answer = []
    arr1 = [1,2,3,4,5]
    arr2 = [2,1,2,3,2,4,2,5]
    arr3 = [3,3,1,1,2,2,4,4,5,5]
    score = []
    
    score1=score2=score3 = 0
    
    for index,num in enumerate(answers):
        if arr1[index%5] == num:
            score1+=1
        if arr2[index%8] == num:
            score2+=1
        if arr3[index%10] == num:
            score3+=1
            
    score.append(score1)
    score.append(score2)
    score.append(score3)
            
    for a,b in enumerate(score):
        if b == max(score):
            answer.append(a+1)
    
    return answer

# 풀이1
def solution(answers):
    p = [[1,2,3,4,5],
        [2,1,2,3,2,4,2,5],
        [3,3,1,1,2,2,4,4,5,5]]
    s = [0] * len(p)

    for q,a in enumerate(answers):
        for i,v in enumerate(p):
            if a == v[q%len(v)]:
                s[i]+=1
    
    return [i+1 for i,v in enumerate(s) if v == max(s)]






