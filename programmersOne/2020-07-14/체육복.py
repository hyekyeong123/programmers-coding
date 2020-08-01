# ***


def solution(n, lost, reserve):
    answer = 0
    for i in range(1, n+1):
        # 사람수는 1부터 시작하니까

        if i not in lost:  # 잃어버리지 않았다면
            answer += 1  # 1 더하기

        else:
            if i in reserve:  # 잃어비렸지만 여분이 있다면
            answer += 1
            reserve.remove(i)  # 여분 삭제
            lost.remove(i)

    # 읽어버렸고 여분도 없어서 남에게 빌려야한다면
    for i in lost:  # 여기에선 반복문의 범위가 len(lost)이다.
        if i-1 in reserve:  # 아랫번호가 가지고 있다면
            answer += 1
            reserve.remove(i-1)
        elif i+1 in reserve:  # 윗 번호가 가지고 있다면
            answer += 1
            reserve.remove(i-1)

    # 잃어버렸고 남에게 빌리지도 못한다면 answer을 증가시키지 않으면 됨

    return answer
