from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    visited = [[False] * m for _ in range(n)]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
 
    def bfs(x, y):
        queue = deque()
        queue.append((x, y))
        days = int(maps[x][y])
        visited[x][y] = True

        while queue:
            x, y = queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny] != 'X':
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    days += int(maps[nx][ny])

        return days

    result = []
    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X' and not visited[i][j]:
                result.append(bfs(i, j))
    result.sort()

    if not result:
        return [-1]
    else:
        return result