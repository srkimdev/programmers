def solution(priorities, location):
    answer = 0
    temp = [0] * len(priorities)
    temp[location] = 1
    
    while priorities:
        first = priorities.pop(0)
        a = temp.pop(0)
        
        if not priorities:
            answer += 1
            break
        
        if first >= max(priorities):
            answer += 1
            if a == 1:
                break
            continue
            
        else:
            priorities.append(first)
            temp.append(a)
    
    return answer