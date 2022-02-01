# 내 풀이(딕셔너링형 값 오름차순으로 정렬)
N = int(input())

dict = {}
for i in range(N):
  input_data = input().split(" ")
  dict[input_data[0]] = input_data[1]

dict = sorted(dict.items(),key = lambda item:item[1])

for score in dict:
  print(score[1],end=" ")


# 풀이1
N = int(input())

array = []
for i in range(N):
  input_data = input().split(" ")
  array.append((input_data[0],int(input_data[1])))

array = sorted(array,key=lambda x: x[1])

for student in array:
  print(student[0],end=' ')
