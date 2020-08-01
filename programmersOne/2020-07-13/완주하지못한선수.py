# 처음 풀이 -> 틀림
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(0, len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[-1]
# 처음에 remove를 사용해서 삭제했는데 아무리 해도 틀린 값이 나왔다.


# 두번째 풀이
participant = ['marina', 'josipa', 'nikola', 'vinko', 'filipa']
completion = ['josipa', 'filipa', 'marina', 'nikola']


def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    for a in participant:
        if a in completion:
            # print("삭제전의 a는 " + a)
            participant.remove(a)
    answer = participant[-1]
    return answer


solution(participant, completion)
# 왜 그런지 찾아보니  remove를 사용하면 반복문을 사용하면서  participant 배열을 그때그때 수정해버리기 때문이다. 그러다보니 인덱스의 순서대로 행하다 스킵하는 부분이 생겨 문제가 발생하는 것......

# 따라서 기존 배열을 망가뜨리는 것보다 새로운 배열을 생성해서 값을 넣는것이 좋다..
