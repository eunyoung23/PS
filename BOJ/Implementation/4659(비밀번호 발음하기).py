import sys

input=sys.stdin.readline

while True:
    word=input().strip()
    flag1=False
    flag2=False
    flag3=False
    if word=='end':
        break
    tests=list(word)
    for test in tests:
        if test in ['a','e','i','o','u']:
            flag1=True
            break
        else:
            pass
    if len(tests)>2:
        for i in range(0,len(tests)-2):
            if tests[i] in ['a','e','i','o','u'] and tests[i+1] in ['a','e','i','o','u'] and tests[i+2] in ['a','e','i','o','u']:
                flag2=False
                break
            else:
                flag2=True
            if tests[i] not in ['a','e','i','o','u'] and tests[i+1] not in ['a','e','i','o','u'] and tests[i+2] not in ['a','e','i','o','u']:
                flag2=False
                break
            else:
                flag2=True
    else:
        flag2=True
    if len(tests)>1:
        for i in range(0,len(tests)-1):
            if tests[i]==tests[i+1] and tests[i]!='e' and tests[i]!='o':
                flag3=False
                break
            else:
                flag3=True
    else:
        flag3=True

    if flag1==True and flag2==True and flag3==True:
        print('<' + word + '>' + " is acceptable.")
    else:
        print('<' + word + '>' + " is not acceptable.")

