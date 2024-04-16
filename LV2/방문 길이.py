def solution(dirs):
    x, y = 0, 0 # 현재 위치

    foot = [] # 발자취, set

    dir = ['R', 'D', 'L', 'U']  #동, 남, 서, 북
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]

    for i in dirs: #ULURRDLLU
        nx = x + dx[dir.index(i)]
        ny = y + dy[dir.index(i)]

        if nx < -5 or nx > 5 or ny < -5 or ny > 5:
            continue

        a = [(x, y), (nx, ny)] # A -> B
        a.sort(key = lambda k : (k[0], k[1]))

        if a not in foot:
            foot.append(a)
        
        x, y = nx, ny

    return len(foot)

