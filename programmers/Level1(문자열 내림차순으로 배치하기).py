# 내 풀이
def solution(s):
    answer = ''
    arr = []
    for letter in s:
        arr.append(ord(letter))
        
    arr.sort(reverse=True)
    for i in arr:
        answer+=(chr(i))
    return answer
  
  
# 다른 풀이1
def solution(s):
    return ''.join(sorted(s,reverse=True))


# 다른 풀이2
def solution(s):
    s = "".join(sorted(s,reverse=True))
    return s
