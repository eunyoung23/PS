# 내 풀이
def solution(arr, divisor):
    answer = []
    for num in arr:
        if num%divisor == 0:
            answer.append(num)
            answer.sort()
    if len(answer) == 0:
        answer.append(-1)
    return answer
  
  
# 다른 풀이1
def solution(arr, divisor):
    return sorted([n for n in arr if n%divisor==0]) or [-1]


# 다른 풀이2
def solution(arr, divisor):
    arr = [x for x in arr if x%divisor == 0]
    arr.sort()
    return arr if len(arr)!=0 else [-1];
