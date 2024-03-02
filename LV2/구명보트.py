from collections import deque

def solution(people, limit):
    people.sort()
    count = 0
    queue = deque(people)

    while queue:
        person = queue.pop()

        if len(queue) > 0 and person + queue[0] <= limit:
            queue.popleft()

        count += 1
    
    return count