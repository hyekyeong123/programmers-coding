def solution(arr):
    result = []
    if len(arr) == 1:
        result.append(-1)
        return result
    else:
        minResult = min(arr)
        arr.remove(minResult)
        return arr
