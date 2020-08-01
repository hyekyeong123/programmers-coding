# 파이썬에서 문자열은 부분적으로 수정이 불가능하다. 따라서 문자열 내용에 수정이 필요하다고 한다면 새롭게 문자열을 생성하는 수 밖에 없다.

# 나의풀이


def solution(phone_number):
    answer = ''
    length = len(phone_number)
    result = phone_number[-4:]  # -4인덱스에서 끝까지

    for i in range(length - 4):
        answer += '*'
    answer = answer+result
    return answer


# 다른 사람의 풀이
# 그러고보니 문자열이 곱셈이 가능하니까 굳이 for문을 돌릴필요가 없다.
for i in range(length - 4):
    answer += '*'
answer = answer+result
return answer
# 이 코드를
return = ('*'*(length - 4))+result 로 변경이 가능하다. 마지막()는 가독성을 위해
