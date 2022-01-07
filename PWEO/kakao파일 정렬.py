```python
# 구현에서 필요한 함수를 구현해서 할 수도 있고....
# 필요한 기본적인 패키지를 불러서 사용할 수 있음...
import re # 정규식을 사용하는데 파이썬에서 사용하는 기본적인 패키지 불러오기

def solution(files):
	answer = []
	##########################
	#01) 우리가 필요한 정보를 담을 새로운 변수: head, number, 원본 순서(index) -> head로 정렬(사전), number(수치), 위치 정보 순서대로...
	my_files = []
	#02) 입력 하나하나에 대해서 처리를 하는데,,, 파일명 + 몇 번째 파일인지 .. -> enumerate
	for idx, i in enumerate(files): # idx: 입력 파일 순서, i: 파일명
		# 2-1) 정규식을 써서 숫자 파트 추출!! -> 0번째만 관심이 있음!!
		number = re.findall("\d+", i) # ["001","002"]
		# 2-2) 숫자파트가 어디서 시작하는지(index메서드를 활용함!)
		# 처음부터 그 number시작 직전가지 싹 긁어서 head파트로...: 슬라이싱
		head = i[:i.index(number[0])
		# 2-3) 각기 head, number에서 원하는 형태로 가공을 해야함!!!(정렬조건때문에!!!)
		# head: 대소문자에 대한 통일(소문자로 통일)
		# number: 0패딩문제 -> int형변환!!
		head = head.lower() # 문자열을 다 소문자로 일괄 변환!
		number = int(number[0]) # 맨 앞에 숫자 덩어리 파트 & 0패딩 제거....
		# 2-4) 우리가 필요한 정보들을 다 처리하고 이제 모아서 쌓자!!!
		my_files.append([head,number,idx]) 
	### -> 모든 입력 파일에 대한 정렬에 대한 필요 정보들 다 처리 완료!!!

	##############
	#03) head, number, 원본 위치 정보를 바탕으로 주어진 조건에 맞춰서 정렬!!!!
	#정렬 : my_files(리스트) -> key, lambda
	my_files.sort(key = lambda x: (x[0],x[1]))
	#############################
	
	#04) 주어진 조건에 맞추서 출력!!!(기준은 입력 데이터 양식으로...)
	for i in my_files:
		answer.append(files[i[2]])
	
	return answer
```
