def solution(s):
    answer = 0

    list = ['zero','one','two','three','four','five','six','seven','eight','nine']

    for i in list:
        s = s.replace(i,str(list.index(i)))

    answer = int(s)

    return answer
