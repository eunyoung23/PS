# 내 풀이
def solution(n):
    answer = 0
    n=list(str(n))
    n.sort(reverse=True)
    answer=int("".join(n))
    return answer
  
# 풀이1
def solution(n):
    answer = ""
    n=list(str(n))
    n.sort(reverse=True)
    for k in n:
        answer+=str(k)
    return int(answer)
