def solution(x):
    sum = 0
    a = x

    # 각 자릿수 가져와서 더하기 로직
    while(a > 0):
        sum += a % 10  # 나머지 더하기 + 3 + 1
        a = a // 10  # 가장 앞자리수 가져오기 # x = 1 x = 0

    if x % sum == 0:
        return True
    else:
        return False
