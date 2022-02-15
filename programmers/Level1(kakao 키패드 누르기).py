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


# 내 풀이
def distance(hand,cos):
    phone={
        "1":(0,0),"2":(1,0),"3":(2,0),
        "4":(0,1),"5":(1,1),"6":(2,1),
        "7":(0,2),"8":(1,2),"9":(2,2),
        "*":(0,3),"0":(1,3),"#":(2,3)
    }
    
    distance=abs(phone[hand][0]-phone[cos][0])+abs(phone[hand][1]-phone[cos][1])
    
    return distance


def solution(numbers, hand):
    answer = ''
    left_hand="*"
    right_hand="#"
    
    for num in numbers:
        if num in [1,4,7]:
            answer+="L"
            left_hand=str(num)
        elif num in [3,6,9]:
            answer+="R"
            right_hand=str(num)
        else:
            left_distance=distance(left_hand,str(num))
            right_distance=distance(right_hand,str(num))
            if left_distance<right_distance:
                answer+="L"
                left_hand=str(num)
            elif left_distance>right_distance:
                answer+="R"
                right_hand=str(num)
            else:
                if hand == "right":
                    answer+="R" 
                    right_hand=str(num)
                elif hand == "left":
                    answer+="L"
                    left_hand=str(num)
    
    return answer
