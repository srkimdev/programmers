#10:30
def solution(storey):

    store = str(storey)
    n = len(store)
    
    result, up = 0, 0
    for i in range(n):
        num = storey % 10
        storey = storey // 10

        if num + up > 5:
            result += 10 - (num + up)
            up = 1

        elif num + up >= 5 and storey % 10 >= 5:
            result += 10 - (num + up)
            up = 1

        elif num + up >= 5 and storey % 10 < 5:
            result += num + up
            up = 0
        else:
            result += num + up
            up = 0
    result += up

    return result

solution(55)