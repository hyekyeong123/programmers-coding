def solution(a, b):
    answer = 0
    if a <= b:
        for i in range(a, b+1):
            answer = answer+i
    else:
        for i in range(b, a+1):
            answer = answer+i
    return answer


# 다른분들의 문제풀이
return sum(range(min(a, b), max(a, b) + 1))
# sum과 min, max를 사용하니까 훨씬 간단하다.
