# 다른 사람의 풀이

# 예를 들어서 a가 3, b가 12라면


def solution(a, b):
    maxResult, minResult = max(a, b), min(a, b)
    # 12 , 3
    t = 1
    while t > 0:
        t = maxResult % minResult
        # 최댓값 나누기 최솟값의 몫이 t
        # t = 4

        maxResult, minResult = minResult, t
        # maxResult = 3, minResult = 4
    answer = [maxResult, int(a*b/maxResult)]
    # 최대 공약수는 3,
    # 최소 공약수는 int(12*3 /3)  = 36 / 3  = 12
    return answer


---------------------------------------------------
a = 2
b = 5

# 예를 들어서 a가 2, b가 5라면


def solution(a, b):
    maxResult, minResult = max(a, b), min(a, b)
    # 5 , 2
    t = 1
    while t > 0:
        t = maxResult % minResult
        # 최댓값 나누기 최솟값의 몫이 t
        # t = 1

        maxResult, minResult = minResult, t
        print("최댓값은 : {}".format(maxResult))
        print("최솟값은 : {}".format(minResult))
        # maxResult = 2, minResult = 1
        # 다시 반복
        # 2 % 1 = 0 t = 0 반복 끝
        # maxResult = 1, minResult = 0

    answer = [maxResult, int(a*b/maxResult)]
    # 최대 공약수는 2,
    # 최소 공약수는 int(2*5 /2)  = 10 / 2  = 5

    # 최대 공약수는 1,
    # 최소 공약수는 int(10 /1)  = 10 / 1  = 10
    return answer


solution(a, b)

# 이건 그냥 수학 덩어리인데..? 혼자서 하라 하면 백퍼 까먹어서 못할듯
