#완전탐색, 그리디인가?
#재귀로 접근 -> 재귀가 아니였음
def solution(n, s):
    if n>s:
        return [-1]
    [portion,remain]=divmod(s,n)
    answer=[portion]*n
    for i in range(remain):
        answer[i]+=1
    return sorted(answer)