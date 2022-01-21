# 입력에 대해서 a1에 대해서 가로, 세로로 분리해서 숫자로...
# 문제에서 보면 파이썬 기준이 아니라 일반적인 인식 기준으로 1부터 시작!!
input_data = "c2"
# 주어진 위치에 대해서 가로, 세로에 대한 값을 각기...
row = int(input_data[1])
column = int(ord(input_data[0])-ord("a")) +1
# print(row)
# print(column)

# L자 이동에 대한 가로 세로에 대한 이동에 대한 정의!!!!!!
steps = [ (-2, -1), (-2, 1), (2,-1),(2,1), 
         (1,-2),(1,2),(-1,-2),(-1,2)]

# 카운팅에 대한 기본 세팅..
result = 0 

# 8가지 L자 이동에 대해서 각기 다 이동시켜보기....
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    # 일단 이동시켰으니, 지도 안인지 밖이지 판단!!!!
    if next_row >=1 and next_row <=8 and next_column >=1 and next_column <=8:
        result +=1
    else: # 지도밖의 경우..
        pass
print(result)
