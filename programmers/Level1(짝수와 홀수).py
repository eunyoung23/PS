# 내 풀이
def solution(num):
    answer = ''
    if num%2==0:
        answer = "Even"
    else:
        answer = "Odd"
    return answer

# 다른 풀이1
def solution(num):
    return "Even" if num%2==0 else "Odd"
