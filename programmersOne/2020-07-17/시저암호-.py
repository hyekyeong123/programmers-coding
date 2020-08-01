import string


def solution(s, n):
    upperCase = string.ascii_uppercase*2
    lowerCase = string.ascii_lowercase*2

    sArray = list(s)
    newArray = []
    for i, v in enumerate(sArray):
        if v in upperCase:
            uIndex = upperCase.find(v)
            uIndex += n
            newArray.append(upperCase[uIndex])
        elif v in lowerCase:
            lIndex = lowerCase.find(v)
            lIndex += n
            newArray.append(lowerCase[lIndex])
        else:
            newArray.append(' ')
    return ''.join(newArray)

# 계속 out of lange 오류가 났던 이유가 z 이상이면 a로 돌아와야하는데 그걸 생각안했었다.


# 다른 사람의 풀이
s = list(s)
   for i in range(s):
        if s[i].isupper():
            s[i] = chr((ord(s[i])-ord('A') + n) % 26+ord('A'))
                                               # 현재 문자열의 아스키값 구하기
            # 대문자 A의 아스키값 빼기
            # n번만큼 이동한 값에
                                               # 나누기 26한것의 몫에다가...그래야지 z를 넘어서도 다시 a부터 시작가능하니까
                                               # A의 값 아스키값 더하기

        elif s[i].islower():
            s[i] = chr((ord(s[i])-ord('a') + n) % 26+ord('a'))

    return "".join(s)
# ------------------------------
ord() 함수: 특정한 한 문자를 아스키 코드 값으로 변환해 주는 함수
chr() 함수: 아스키 코드 값을 문자로 변환해 주는 함수 (10진수, 16진수 사용 가능)
