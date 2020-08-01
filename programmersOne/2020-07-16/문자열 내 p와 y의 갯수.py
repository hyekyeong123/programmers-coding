def solution(s):
    sArray = []
    pcount = 0
    ycount = 0
    sArray = list(s)

    for i in sArray:
        if i == 'p' or i == 'P':
            pcount += 1
        elif i == 'y' or i == 'Y':
            ycount += 1
            # 파이썬은 후위연산자 ++ 사용안함
    if pcount == 0 and ycount == 0:
        return False
        # 앞에만 대문자
    if pcount == ycount:
        return True
    else:
        return False
