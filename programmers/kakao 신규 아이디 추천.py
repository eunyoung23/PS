import re

def solution(new_id):
    answer = ''
  
    #1단계 : new_id의 모든 대문자를 대응되는 소문자로 치환함
    answer = new_id.lower()

    #2단계: 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한     #모든 문자를 제거함
    for value in answer:
      if value.islower() or value.isdigit() or value in ["-","_","."]:
        answer+=value

    #3단계: '..'와 '..'가 '.'로 바뀜
    while '..' in answer:
      answer = answer.replace('..','.')

    #4단계: 아이디의 처음에 위치한 '.'가 제거됨
    answer = answer.strip('.')

    #5단계: 아이디가 빈 문자열이면, new_id에 "a"를 대입함
    if answer=="":
      answer+='a'

    #6단계: 길이가 16자 이상이라면, new_id의 첫 15개의 문자를 제외한 
    #나머지 문자들을 모두 제거함, 제거후 마침표(.)가 끝에 위치하면 이것도
    # 제거함
    if len(answer)>=16:
      answer = answer[:15]
      answer = answer.rstrip('.')

    #7단계: 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이
    #가 3이 될때까지 반복해서 붙임
    if len(answer)<=2:
      new = answer[len(answer)-1:]
      while len(answer)<3:
        answer+=new
  
    return answer
