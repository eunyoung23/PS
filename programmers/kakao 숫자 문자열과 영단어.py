def solution(s):
  answer = 0

  words = ["zero","one","two","three","four","five","six","seven","eight","nine"]

  for i in words:
    s = s.replace(i,str(words.index(i)))

  answer = s

  return answer
