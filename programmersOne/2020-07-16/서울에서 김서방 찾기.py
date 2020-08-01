def solution(seoul):
    answer = ''
    for i, v in enumerate(seoul):
        if v == 'Kim':
            answer = '김서방은 {}에 있다' .format(i)
    return answer
