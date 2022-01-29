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

# 다른 풀이 1
def solution(array, commands):
    answer = []
    for command in commands:
      tmp_arr = array[(command[0]-1):command[1]]
      tmp_arr.sort()
      num = tmp_arr[command[2]-1]
      answer.append(num)
    return answer

# 다른 풀이 2
def solution(array,commands):
  answer = []
  for com in commands:
    answer.append(sorted(array[com[0]-1:com[1]])[com[2]-1])

  return answer
