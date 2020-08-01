# 값을 집어넣을때 자꾸 틀림
n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]


def solution(n, arr1, arr2):
    answer = []
    newArray = []
    bin1Result = []
    bin2Result = []
    bin1ResultArray = []
    bin1ResultArray = []
    newArrayArray = []
    for i in range(n):
        # 그러고보니 2진수에는 0b가 붇음 이거 제외해야함
        bin1Result.append(bin(arr1[i])[2:])
        # 2진수로 변환하기
        bin2Result.append(bin(arr2[i])[2:])
        bin1ResultArray = str(bin1Result)
        print(bin1ResultArray)
        bin2ResultArray = str(bin2Result)

        for j in range(len(bin1ResultArray[i])):
            if bin1ResultArray[i][j] == 0 and bin2ResultArray[i][j] == 0:
                newArray.append('#')
            elif bin1ResultArray[i][j] == 1 or bin2ResultArray[i][j] == 1:
                newArray.append('')

    return newArray


solution(n, arr1, arr2)

# 다른 사람의 풀이


def solution(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        a12 = str(bin(i | j)[2:])
        a12 = a12.rjust(n, '0')
        a12 = a12.replace('1', '#')
        a12 = a12.replace('0', ' ')
        answer.append(a12)
    return answer
