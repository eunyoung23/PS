# 내 풀이
a, b = map(int, input().strip().split(' '))
result=""
for _ in range(b):
    result=""
    for _ in range(a):
        result+="*"
    print(result)
    
# 다른 풀이1
a, b = map(int, input().strip().split(' '))

for i in range(b):
  for j in range(a):
    print("*",end='')
  print('')

# 다른 풀이2
a, b = map(int, input().strip().split(' '))
answer = ('*'*a+'\n')*b
print(answer)
