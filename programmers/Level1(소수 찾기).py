#case1 : 이 방식대로 했더니 시간 초과 남 -> n의 범위가  백만으로 너무 많긴 함.
def solution(n):
    answer = 0

    for num in range(2, n + 1):
        cnt = 0
        for i in range(1, num + 1):
            if num % i == 0:
                cnt += 1
        if cnt == 2:
            answer += 1

    return answer

#case2 -> 에라토스테네스의 체로 풀기
def solution(n):
    num = set(range(2, n + 1))

    for i in range(2, n + 1):
        if i in num:
            num -= set(range(2 * i, n + 1, i))

    return len(num)
