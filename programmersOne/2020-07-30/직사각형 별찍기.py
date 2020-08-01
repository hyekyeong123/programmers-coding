m, n = map(int, input().strip().split(' '))
for i in range(n):
    print('*'*m)

# 다른 사람의 풀이
answer = ('*' * a + '\n') * b

- strip()에다가 인자를 넣지 않으면 문자열 처음과 끝에 공백 제거
- 이후 문자열을 정수로 변환 map(int, ["5", "3"])
