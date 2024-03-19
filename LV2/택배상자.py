def solution(order):
    stack = []
    i, count = 1, 0

    while i != len(order) + 1:
        stack.append(i)
        
        while stack and stack[-1] == order[count]:
            stack.pop()
            count += 1

        i += 1

    return count

