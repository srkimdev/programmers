from collections import deque

def solution(maps):
    answer = 0

    n = len(maps)
    m = len(maps[0])

    INF = int(1e9)
    
    dp = [[INF] * m for _ in range(n)]
    dp[0][0] = 1

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    def bfs(x, y):
        queue = deque()
        queue.append((x, y))

        while queue:
            x, y = queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                    queue.append((nx, ny))
                    maps[nx][ny] = maps[x][y] + 1
                    dp[nx][ny] = min(dp[nx][ny], dp[x][y] + 1)

    
    bfs(0, 0)
    # print(dp[n - 1][m - 1])
    if dp[n - 1][m - 1] == INF:
        return -1
    else:
        return dp[n - 1][m - 1]

solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])