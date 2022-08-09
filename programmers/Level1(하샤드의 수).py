def solution(x):
    answer = True
    num=x
    sum=0
    
    while x!=0:
        sum+=x%10
        x=x//10
        
    result=num%sum
    
    if result==0:
        return True
    else:
        return False
