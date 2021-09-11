# 집합으로 푼 
arr = set()
for _ in range(0,10):
    N = int(input())
    arr.add(N%42)

print(len(arr))

#리스트로 푼거
num_list = [0 for i in range(42)]
for i in range(10):
    num_list[int(input()) % 42] +=1

num_list = [x for x in num_list if x!=0]
print(len(num_list))
