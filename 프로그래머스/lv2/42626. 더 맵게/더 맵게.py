from heapq import *

def solution(scoville, K):
    answer = 0
    heapify(scoville)
    
    while scoville[0]<K and len(scoville)>1:
        num1=heappop(scoville)
        num2=heappop(scoville)
        heappush(scoville,num1+num2*2)
        answer+=1
    
    return answer if scoville[0]>=K else -1