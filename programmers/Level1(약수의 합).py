# 내 풀이

def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i==0:
            answer+=i
    return answer
  
# 풀이1
def solution(n):
    return sum([i for i in range(1,n+1) if n%i==0])
