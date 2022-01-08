def solution(numbers, hand):
    answer = ''
   
    # 1) 왼손, 오른손에 대한 위치에 대한 초기화.
    left_pos = "*"
    right_pos = "#"
    # 2) 이 사람이 오른손잡이, 외손잡인지에 대한 기준손!!!!!
    if hand == "right": # 비교 연산자 ==
        hand = "R"       # 대입연산자 =
    elif hand == "left":
        hand ="L"
    else:
        print("Error~~~~")
    
    # 3) 본격적으로 할 부분은 : 입력으로 받은 numbers 돌아가면서...
    for num in numbers:
        # case1) 무조건 왼손으로만
        if num in [1, 4, 7]:
            answer +="L"
            left_pos = str(num)
            continue
        # case2) 무조건 오른손으로만
        elif num in [3,6,9]:
            answer += "R"
            right_pos = str(num)
            continue
        # case3) 거리를 계산
        elif num in [2,5,8,0]:
            # num(2,m5,8,0중 하나의 수)과
            # 왼손,오른손의 거리 값!!!!
            # 거리를 계산하는 함수 : 입력[손 위치, 눌러야할 번호] - 거리
            dis_left = get_distance(num,left_pos)
            dis_right = get_distance(num, right_pos)
        #   case3-1) L < R -> L
            if dis_left < dis_right:
                answer += "L"
                left_pos = str(num)
        #   case3-2) L > R -> R
            elif dis_left > dis_right:
                answer += "R"
                right_pos = str(num)
        #   case3-3) L = R -> hand(기준 손)
            elif dis_left == dis_right:
                answer += hand
                if hand =="L":
                    left_pos = str(num)
                elif hand =="R":
                    right_pos = str(num)

    return answer
