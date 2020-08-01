arr = [4, 4, 4, 3, 3]


def solution(s):
    a = []

    # -------------
    for i in s:
        if a[-1:] == [i]:
            continue
        # 같은 경우 건너뛰기

        a.append(i)
        # 같지 않은것만 appedn하기
    return a


    # -------------
solution(arr)

# 이렇게도------------------------------------
for i in s:
    if (len(a) == 0) or (a[-1] != i):
        a.append(i)
return a

# 반복문 안에서 del이나 remove 쓰는것 안좋다는걸 저번에 배웠는데도 또....
