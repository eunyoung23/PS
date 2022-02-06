# 내 풀이
def solution(seoul):
    answer = ''
    for i in seoul:
        if i == "Kim":
            num = seoul.index(i)
    answer = '김서방은 %d에 있다'%num
    return answer
  
# 풀이1
def solution(seoul):
  return "김서방은 {}에 있다".format(seoul.index("Kim"))

