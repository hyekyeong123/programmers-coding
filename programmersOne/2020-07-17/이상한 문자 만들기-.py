def solution(s):
    newStr = ''
    sArray = s.split(" ")
    for i, v in enumerate(sArray):
        # 3번 반복
        vArray = list(v)  # 각 문자열을 리스트로 만들기
        for ii, vv in enumerate(vArray):
            if ii == 0:
                newStr += vv.upper()
            elif ii % 2 == 0:
                # 짝수라면
                newStr += vv.upper()
            else:
                newStr += vv.lower()
        if i != len(sArray)-1:  # 만약에 마지막이 아니라면
            newStr += ' '  # 각 단어 사이 띄어쓰기
    return newStr

# upper와 lower은 반드시 새로운값에다가 저장해야지만 유지됨
# 배열이라면 append 사용하기
