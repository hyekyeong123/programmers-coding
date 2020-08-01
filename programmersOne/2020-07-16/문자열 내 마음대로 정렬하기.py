

# 다른분들의 문제풀이
def solution(strings, n):
    return sorted([s for s in strings], key=lambda a: [a[n], a])

# 이건 솔직히 해석이 안되어서 가져와봤다...
# 실제 실무에서도 람다식을 많이 쓸까..?
