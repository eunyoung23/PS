#각 배열에 숫자가 나온 횟수가 저장되어 있어야 할거 같으므로 해시맵 구조를 이용하면 될거 같음.
#딕셔너리 값 내림차순으로 정렬하기 근데 인덱스 순으로도 정렬해야함.
import sys

input=sys.stdin.readline

N,C=map(int,input().split())

arr=list(map(int,input().split()))
dict={}

for i in range(N):
    if arr[i] in dict:
        dict[arr[i]][0]+=1
    else:
        dict[arr[i]]=[1,i]

dict=sorted(dict.items(),key=lambda x:(-x[1][0],x[1][1]))

for number in dict:
    for num in range(number[1][0]):
        print(number[0],end=" ")
