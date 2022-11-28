def solution(s):
    #문자열에 결과를 저장할 변수
    result = ''
    #한 단어를 임시로 저장할 변수
    word=''
    
    for char in s:
        #문자가 공백문자인 경우
        if char==" ":
            if word!="":
                word=word[0].upper()+word[1:]
                result+=word
                word=""
            result+=" "
        else:
            #문자가 공백문자가 아니라면
            word+=char.lower()
    
    if word!="":
        word=word[0].upper()+word[1:]
        result+=word
    
    return result