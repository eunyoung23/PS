# 내 풀이
def solution(s):
    answer = ''
    num = len(s)
    if num%2==0:
        answer = s[(num//2)-1:(num//2)+1]
    else:
        answer = s[num//2]
        
    return answer
  
  
  # 다른 풀이1
  def solution(s): 
    return s[(len(s)-1)//2:len(s)//2+1]
  
  
 
