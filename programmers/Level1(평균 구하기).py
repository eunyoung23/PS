#내 풀이
def solution(arr):
    answer = sum(arr)/len(arr)
    return answer
 
# 다른 풀이1
def solution(list):
    if len(list) == 0:
        return 0

    return sum(list) / len(list)


# 다른 풀이2
import statistics

def solution(list):
    return statistics.mean(list)
