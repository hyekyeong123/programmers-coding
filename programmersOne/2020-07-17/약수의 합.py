def solution(n):
    answer = 0
    for i in range(1, n+1):  # 자기 자신의 값도 더해줘야함
        if n % i == 0:
            answer += i
    return answer
