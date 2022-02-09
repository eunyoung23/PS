# 내 풀이
def solution(strings, n):
    return sorted(sorted(strings),key=lambda x : x[n])

# 풀이1
def solution(strings, n):
    new = []
    for i in strings:
        new.append(i[n]+i)
    new.sort()
    answer = []
    for i in new:
        answer.append(i[1:])
    return answer
