# 코테 특강 풀이1
# 기본적인 변수들 선언
n = 5 
x, y = 1, 1 # 위치에 대한 초기값...(문제에서 1,1에서 항상 시작한다고 함.)

plans = ["R","R","R","U","D","D"] # 이동 지시사항..

# 이동방향 LRUD
move_types = ["L","R","U","D"]
# 그 이동에 대한 x, y좌표상에서 이동에 대한 룰...
dx = [0, 0, -1, 1]
dy = [-1,1, 0, 0]

# 지시사항대로 다 수행을 해야함!! - for문을 써서
# 이동하면서,,,, 지도 안이냐 밖이냐 - if문을 써서
for plan in plans:
# 어떤 이동 지시 사항인지 찾아보기 : move_types -> dx,dy 순서 정보 같이 활용
	for i in range(len(move_types)):
		if plan == move_types[i]:
# 일단 지시사항대로 이동시켜보기....
			nx = x + dx[i]
			ny = y + dy[i]
		else:
			pass
# 일단 이동시켜 본 위치의 정보는 nx,ny -> 지동 안이면 진짜 이동 ! / 지도 밖이면 이동을 안함!
		if nx < 1 or nx > n or ny < 1 or ny > n :
			continue
		else: # 지시 사항대로 이동 시킬 때, 지도 안에 존재하는 경우!!
			x = nx
			y = ny
print(x,y)

#코테 특강 풀이2 - 딕셔너리
n = int(input("지도의 크기를 입력하세요."))
x,y=1,1

plans = list(input("이동 게획을 입력하세요."))

move = {"L":[0,-1],"R":[0,1],"U":[-1,0],"D":[1,0]}

for plan in plans:
  dx,dy = move[plan]
  nx = x+dx
  ny = y+dy

  if nx<1 or nx>n or ny<1 or ny>n:
    continue
  else:
    x=nx
    y=ny

print(x,y)


#내 풀이(이동시켜본 위치 좌표 확인하는 방법으로 -> 지도 안이면 진짜 이동 / 아니면 이동을 안함!)
N = int(input())
x,y=1,1
move = input().split()

dx = [0,0,-1,1]
dy = [-1,1,0,0]

for i in move:
  if i == "L":
    nx = x+dx[0]
    ny = y+dy[0]
  elif i == "R":
    nx = x+dx[1]
    ny = y+dy[1]
  elif i == "U":
    nx = x+dx[2]
    ny = y+dy[2]
  else:
    nx = x+dx[3]
    ny = y+dy[3]
  if nx<1 or ny<1 or nx>N or ny>N:
    continue
  x,y = nx,ny
    
print(x,y)

#책 풀이
N = int(input())
x,y = 1,1
plans = input().split()

dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L','R','U','D']

for plan in plans:
  for i in range(len(move_types)):
    if plan == move_types[i]:
      nx = x+dx[i]
      ny = y+dy[i]
  if nx<1 or ny<1 or nx>N or ny>N:
    continue
  x,y= nx,ny

print(x,y)



