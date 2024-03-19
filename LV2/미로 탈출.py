#6:13
from collections import deque

def solution(maps):
    L_x, L_y, S_x, S_y = 0, 0, 0, 0

    n = len(maps)
    m = len(maps[0])

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'L':
                L_x = i
                L_y = j

            elif maps[i][j] == 'S':
                S_x = i
                S_y = j

            elif maps[i][j] == 'E':
                E_x = i
                E_y = j

    def bfs(x, y):
        queue = deque()
        queue.append((x, y))
        foot_print = [[0] * m for _ in range(n)]
        foot_print[x][y] = True

        while queue:
            x, y = queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < m and not maps[nx][ny] == 'X' and not foot_print[nx][ny]:
                    queue.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
                    foot_print[nx][ny] = True


    visited = [[0] * m for _ in range(n)]
    bfs(S_x, S_y)
    result1 = visited[L_x][L_y]

    visited = [[0] * m for _ in range(n)]
    bfs(L_x, L_y)
    result2 = visited[E_x][E_y]

    if result1 and result2:
        return result1 + result2
    else:
        return -1