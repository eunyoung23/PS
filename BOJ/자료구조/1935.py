N = int(input())
sen = input()
alpha = [0]*N
stack = []

for i in range(N):
    alpha[i] = int(input())


for i in sen:
    if 'A'<=i<='Z':
        stack.append(alpha[ord(i)-ord('A')])
    else:
        str2 = stack.pop()
        str1 = stack.pop()

        if i == '+':
            result=str1+str2
        elif i == '*':
            result=str1*str2
        elif i=='/':
            result=str1/str2
        else:
            result=str1-str2
        stack.append(result)


print('%.2f'%stack[0])
