# 내 풀이
def solution(array, commands):
    i = 0
    num = len(commands)
    answer = []
    while i<num:
        start = commands[i][0]
        end = commands[i][1]
        point = commands[i][2]
        arr = array[start-1:end]
        arr.sort()
        answer.append(arr[point-1])
        i+=1

    return answer
