def solution(num):
    answer = ''
    if num % 2 == 0:
        answer = 'Even'
    else:
        answer = 'Odd'
    return answer


# 다른 사람의 풀이

return ["Even", "Odd"][num & 1]
# 2진비트가 1번째 비트자리에 의해 홀짝이 결정
# & 연산자로 0 과 1을 구해 리스트 인덱스로 된 것
# 왜냐면 이진법에서는 뒷자리가 1이라면 1을 더해야 하기 때문에
# num & 1이 1이라면 ["Even", "Odd"]의 0번째 자리 가져오기 - 홀수(Odd)
# num & 1이 0이라면 ["Even", "Odd"]의 0번째 자리 가져오기 - 짝수(Even)
