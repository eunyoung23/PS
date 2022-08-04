# 내 풀이
def solution(a, b):
    answer = ''
    cal = 0

    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    week = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]

    for i in range(0, a - 1):
        cal += days[i]

    cal += b

    answer = week[cal % 7]

    return answer
