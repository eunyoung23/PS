#case1
def solution(numbers):
    answer = []

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            sum = numbers[i] + numbers[j]
            if sum not in answer:
                answer.append(sum)

    answer.sort()

    return answer

#case2
from itertools import combinations


def solution(numbers):
    answer = []
    arr = combinations(numbers, 2)

    for number in arr:
        num = number[0] + number[1]
        if num in answer:
            pass
        else:
            answer.append(num)

    answer.sort()

    return answer
