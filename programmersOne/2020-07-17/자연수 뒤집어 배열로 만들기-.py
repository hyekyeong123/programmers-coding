def solution(n):
    answer = []
    nStr = str(n)
    answer = list(nStr[::-1])  # reverse와 동일
    return [int(i) for i in answer]
