def solution(x, n):
    answer = []
    for i in range(n):
        answer.append(x + x*i)
    return answer


# 다른 사람의 풀이
return [i * x + x for i in range(n)
