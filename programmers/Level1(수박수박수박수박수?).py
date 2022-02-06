# 내 풀이
def solution(n):
    answer = ''
    for i in range(n):
        if i%2==0:
            answer+="수"
        else:
            answer+="박"
    return answer
  
  
# 풀이1
def solution(n):
  s = "수박" * n
  return s[:n]
