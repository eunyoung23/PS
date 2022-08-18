#35분->50
#1. word의 각 알파벳의 개수 알아내기(o)
#2. 그것을 통해 팰린드롬이 가능한지 알아내기(O) - 홀수인 알파벳이 두개 이상이면 팰린드롬이 될 수 없음.
#3. 팰린드롬 만들기
import sys

input=sys.stdin.readline

words=input().strip()
words_cnt=[0 for _ in range(26)]

for word in words:
    words_cnt[ord(word)-65]+=1

odd=0
odd_alpha=''
alpha=''
for i in range(26):
    if words_cnt[i]%2==1:
        odd+=1
        odd_alpha+=chr(i+65)
    alpha=chr(i+65)*(words_cnt[i]//2)

if odd>1:
    print("I'm Sorry Hansoo")
else:
    print(alpha+odd_alpha+alpha[::-1])
