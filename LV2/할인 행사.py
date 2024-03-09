from collections import deque

def solution(want, number, discount):
    answer = 0
    queue = deque(discount[:10])
    j = 10

    while j <= len(discount):
        for i in range(len(want)):
            if queue.count(want[i]) != number[i]:
                break

        else:
            answer += 1

        if j != len(discount):
            queue.popleft()
            queue.append(discount[j])
        j += 1

    return answer