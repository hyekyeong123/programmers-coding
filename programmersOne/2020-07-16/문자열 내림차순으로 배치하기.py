def solution(s):
    answer = ''
    s_array = sorted(list(s), reverse=True)
    return ''.join(s_array)
