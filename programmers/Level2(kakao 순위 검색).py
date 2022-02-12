# 내 풀이
def solution(info, query):
    answer = [0]*len(query)
    question = []
    result = []
    result2 = []
    
    for str in info:
        result.append(str.split(" "))
    
    for str in query:
        question.append(" ".join(str.split(" and ")))
    
    for array in question:
        result2.append(array.split(" "))

# -이 나오면은!
    for a in range(len(result2)):
        for b in range(len(result)):
            flag=0
            for i in range(4):
                if result[b][i]!=result2[a][i]:
                    if result2[a][i] != "-":
                        flag=1
                        break
            if flag == 0:
                if int(result[b][4]) >= int(result2[a][4]):
                    answer[a]+=1
        
    return answer
