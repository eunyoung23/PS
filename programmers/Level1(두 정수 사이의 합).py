# 내 풀이
def solution(a, b):
    answer = 0
    if a<b:
        arr = [x for x in range(a,b+1)]
    else:
        arr = [x for x in range(b,a+1)]
    answer = sum(arr)
    return answer
  
# 다른 풀이1
def solution(a, b): 
    if a>b: a,b = b,a
    return sum(range(a,b+1))


# 다른 풀이2
def solution(a, b):
    return (abs(a-b)+1)*(a+b)//2
