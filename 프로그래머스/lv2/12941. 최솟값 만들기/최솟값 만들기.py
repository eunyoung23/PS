'''
완전 탐색 문제인거 같음  - 근데 이러면 시간초과 날거 같긴함.
배열에서 어떻게 섞어서 계산을 할까 - 배열 한개를 오름차순, 배열 한개를 내림차순으로 정렬하면 되긴 함.
'''
def solution(A,B):
    answer = 0

    A.sort()
    B.sort(reverse=True)
    
    for idx in range(len(A)):
        answer+=A[idx]*B[idx]

    return answer