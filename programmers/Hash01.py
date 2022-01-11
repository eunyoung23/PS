def solution(participant,completion):
		answer = ''
		#############################
		# 처리할 변수의 자료유형을 dict -> 이름: key, 사람수 : value
		people_dict = {}
		# 참가자들을: +
		for p in participant:
				if p in people_dict : # 이미 같은 이름의 사람이 있다면 : +1 업데이트
						people_dict[p] += 1
				else: # 아직 동일한 이름이 등록되지 않은 사람인 경우
						people_dict[p] = 1
		
		# 완주자들을 처리를 : -
		for p in completion:
				if people_dict[p] == 1: # 지금 그 이름에 대해서 존재한 사람이 1이면서 1명 완주했다면..
					del people_dict[p]
				else: # 동명이인이 존재할 경우....
					people_dict[p] -= 1

		# 출력!! people_dict는 dict형...
		answer = list(people_dict.keys())[0]

		return answer
