# ***
def solution(answers):
    person = [[1, 2, 3, 4, 5],
              [2, 1, 2, 3, 2, 4, 2, 5],
              [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    s = [0] * len(p)

    for q, a in enumerate(answers):
        # q = 10000
        for i, v in enumerate(person):
            # 예를 들어 v[0] = [1, 2, 3, 4, 5]
            if a == v[q % len(v)]:
                s[i] += 1
    return [i + 1 for i, v in enumerate(s) if v == max(s)]
    # for 문 앞에 쓰면 바로 append 해 주는 파이썬 기능인듯
