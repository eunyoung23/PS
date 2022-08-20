#2중 for문 안에 if문이 있을때 break문
# 19번째의 break문은 j에 대한 for문을 탈출하기 ㅜ이해서 사용됨.따라서 i에 대한 for문에서 아직 탈출하지 못했기 때문에 리스트에 7명이 남았음에도 불구하고 계속 돌아감
# 따라서 20,21번 줄 처리 또는 flag 처리를 꼭 해줘야 함.
# 실제 반레:
# Input : [1,9,2,8,3,7,4,6,70]
# Output : [2,4,6,8,70]
# Answer : [2,3,4,5,6,7,8,70]
import sys

input=sys.stdin.readline

height=[]

for _ in range(9):
    height.append(int(input()))

for i in range(0,len(height)-1):
    for j in range(i+1,len(height)):
        num1=height[i]
        num2=height[j]
        if sum(height)-(num1+num2)==100:
            height.remove(num1)
            height.remove(num2)
            break
    if len(height)<9:
        break

height.sort()

for num in height:
    print(num)
