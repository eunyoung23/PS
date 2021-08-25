for _ in range(int(input())):
    stk = []
    is_vps = True
    for ch in input():
        if ch == "(":
            stk.append(ch)
        else:
            if stk:
                stk.pop()
            else:
                is_vps=False
                break

    if stk:
        is_vps = False

    print("Yes" if is_vps else "NO")
