def solution(num):
    answer = 0
    for i in range(500):

        if num == 1:
            return answer
            # 반드시 맨 처음에 넣어야함 안그러면 오류 발생

        if i == 499 and num != 1:
            # 500번 반복해도 num이 1이 아니라면
            return -1

        if num % 2 == 0:
            # 짝수라면
            num = num / 2
            answer += 1
        else:
            # 홀수라면
            num = num * 3 + 1
            answer += 1
