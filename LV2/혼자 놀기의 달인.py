def solution(cards):
    visited = [False] * len(cards)
    arr = []
    
    def dfs(box, x, visited):

        if visited[x] == True:
            return box
        
        else:
            box += 1
            visited[x] = True
            return dfs(box, cards[x] - 1, visited)

    
    for i in range(len(cards)):
        
        if visited[i] == True:
            continue

        else:
            box = 0
            arr.append(dfs(box, i, visited))
            print(visited)
    
    if len(arr) == 1:
        return 0

    arr.sort(reverse = True)

    answer = arr[0] * arr[1]
        
    return answer