def check(n):
    div=1
    while True:
        if div%n==0:
            return len(str(div))
        else:
            div=div*10+1

while True:
    try:
        n=int(input())
        print(check(n))
    except:
        break
