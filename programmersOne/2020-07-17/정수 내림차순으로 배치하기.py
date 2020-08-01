def solution(n):
    nStr = sorted(list(str(n)), reverse=True)
    return int(''.join(nStr))
