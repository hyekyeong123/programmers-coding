def solution(d, budget):
    d.sort()
    answer = 0
    sumResult = 0
    for i, v in enumerate(d):
        sumResult += v  # 일단 더한후에
        if(budget >= sumResult):
            answer += 1   # 작으면 1더하기
    return answer
