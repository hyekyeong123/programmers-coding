# 예로 들어  n이 987이라고 하자
def solution(n):
    result = 0
    while(n != 0):
        result += (n % 10)  # 나머지는 7
        n = n//10
        # 987을 10으로 나누면 98.7인데 정수로하면 98
    return result
