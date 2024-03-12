# 5:55
from collections import deque

def solution(k, tangerine):

    dic = {}
    for i in range(len(tangerine)):
        dic[tangerine[i]] = dic.get(tangerine[i], 0) + 1

    dic = dict(sorted(dic.items(), key = lambda x : x[1]))

    queue = deque()
    for i in dic.values():
        queue.append(i)

    for _ in range(len(tangerine) - k):
        queue[0] -= 1

        if queue[0] == 0:
            queue.popleft()

    answer = len(queue)
    return answer


