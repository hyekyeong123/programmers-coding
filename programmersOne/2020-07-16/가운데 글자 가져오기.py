def solution(s):
    answer = ''
    first = len(s) // 2
    #  만약에 4라면 2, 5라면 2, 6이라면 3
    if(len(s) % 2 == 0):
        # 짝수
        answer = s[first-1:first+1]
    else:
        answer = s[first]
    return answer
