#case1
def solution(phone_number):
    num = len(phone_number[:-4])
    for i in range(num):
        phone_number=phone_number.replace(phone_number[i],"*",1)
    return phone_number

#case2
def solution(phone_number):
    answer = ''

    for i in range(0, len(phone_number) - 4):
        answer += "*"

    answer += phone_number[-4:]

    return answer


#case3
def solution(phone_number):
    answer = ''

    for num in range(len(phone_number[:-4])):
        answer += "*"

    answer += phone_number[-4:]

    return answer
