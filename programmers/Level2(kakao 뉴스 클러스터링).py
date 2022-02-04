# 내 풀이
from collections import Counter

def solution(str1, str2):
    answer = 0
    arr=list()
    arr2=list()
    
    for i in range(0,len(str1)-1):
        if str1[i:i+2].isalpha():
            arr.append(str1[i:i+2].upper())
        else:
            continue
       
    for i in range(0,len(str2)-1):
        if str2[i:i+2].isalpha():
            arr2.append(str2[i:i+2].upper())
        else:
            continue
    
    inter = list((Counter(arr)|Counter(arr2)).elements())
    union = list((Counter(arr)&Counter(arr2)).elements())
    
    if len(inter)==0 or len(union)==0:
        answer=65536
    else:
        answer=int(65536*(len(inter)/len(union))
    
return answer
