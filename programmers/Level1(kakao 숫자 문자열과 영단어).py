def solution(s):
    answer = 0

    list = ['zero','one','two','three','four','five','six','seven','eight','nine']

    for i in list:
        s = s.replace(i,str(list.index(i)))

    answer = int(s)

    return answer

# 내 풀이
def solution(s):
    answer = 0
    
    arr = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    
    
    for num in arr:
        if num in s:
            replace = arr.index(num)
            s=s.replace(num,str(replace))
    
    answer= int(s)
    
    return answer
