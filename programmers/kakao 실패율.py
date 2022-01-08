def solution(N, stages):
    answer = []
    ###############
    # 1) 필요한 것이 stage별 실패율을 기록할 변수
    fail_dict = {}
    num_people = len(stages) #전체 참가자 수..
    
    # 2) 1번 stage~~N번 stage까지 stage를 기준으로 돌리면서.....참가자, 실패, 성공자 = 다음 스테이지 참가자..
    for stage in range(1, N+1):
        # 실패자 : 그 스테이지의 값의 수!
        fail_num =  stages.count(stage)
        # 실패율 계산
        if num_people > 0 : # 1명 이상의 참가자가 있는 경우
            fail_dict[stage] = fail_num / num_people
        else: # 참가자 0명 -> 정의를 0으로 정의함!
            fail_dict[stage] = 0
        # 다음  stage.에 참가할 인원 정보를 갱신해서 넘겨줘야 함!
        num_people = num_people - fail_num
    
    # 3) 이제 정보들을 다 수집했으니,,,정렬
    fail_dict = sorted(fail_dict.items(), key = lambda x : x[1], reverse=True)

    # 4) 정렬된 상태에서 스테이지 번호들만....단, 실패율이 같으면,,,순서대로.
    # ------> 리스트 컴프리 핸션을 써서...
    answer = [ s_info[0] for s_info in fail_dict]


    return answer
