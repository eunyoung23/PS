# 내 풀이
def solution(s):
    if (len(s)==4 or len(s)==6) and s.isdigit():
        answer = True
    else:
        answer = False
    return answer


# 다른 풀이1
def solution(s):
    return s.isdigit() and len(s) in (4,6)

# 다른 풀이2
def solution(s):
    return s.isdigit() and (len(s)==4 or len(s) == 6)




