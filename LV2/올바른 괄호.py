def solution(s):
    stack = []
    
    for i in s:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if stack:
                stack.pop()
            else:
                stack.append(i)

    if not stack:
        return True
    else:
        return False
    
print(solution(')'))