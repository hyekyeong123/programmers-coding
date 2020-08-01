arr1 = [[1, 2], [2, 3]]
arr2 = [[3, 4], [5, 6]]


def solution(arr1, arr2):
    print(arr1[0])
    for i in range(len(arr1)):
        # print(i)
        # 0, 1
        print(arr1[0])
        # [1, 2]
        # [4, 6]

        for j in range(len(arr1[0])):
            arr1[i][j] += arr2[i][j]
    return arr1


solution(arr1, arr2)
