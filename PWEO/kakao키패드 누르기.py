def get_distance(num, hand):
    # 키패드에 대한 구현 -> 거리 계산을!!!
    key_pos = {
        "1" : (0,0), "2":(0,1), "3":(0,2),
        "4" : (1,0), "5":(1,1), "6":(1,2),
        "7" : (2,0), "8":(2,1), "9":(2,2),
        "*" : (3,0), "0":(3,1), "#" :(3,2) 
    }
    num = str(num)
    # 지급 입력을 요청한 손이 있는 hand에대 좌표
    x_hand, y_hand = key_pos[hand]
    # 눌러야하는 2580중 타겟 패드에 대한 좌표.
    x_num, y_num = key_pos[num]
    # 거리 계산 : x, y -> abs()함수!!!
    return abs(x_hand - x_num) + abs(y_hand - y_num)
  
  
  def solution(numbers, hand):
    answer = ''
    ###############
    # 1) 왼손, 오른손에 대한 위치에 대한 초기화.(왼손, 오른손 위치.)
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
        # case3) 거리를 계산해야한다...
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

    ##############
    return answer
