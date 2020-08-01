import math


def solution(n):
    result = math.sqrt(n)
                               # 루트값 구하기

    if result.is_integer():
        # is_integer은 끝에 0이 붙어도 정수이면 True 반환
        return int((result+1)**2)
    else:
        return - 1


# 다른 사람의 풀이
sqrt = n ** (1/2)
                       # 이렇게 하면 math.sqrt(n)를 할 필요가 없어진다. 왜 그생각을 못했지
   if sqrt % 1 == 0:
        return (sqrt + 1) ** 2
    return 'no'
