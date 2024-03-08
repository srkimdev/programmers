def solution(picks, minerals):
    answer = 0
    
    if sum(picks) * 5 < len(minerals):
        minerals = minerals[:sum(picks) * 5]
    
    mineral_count = [[0, 0, 0] for _ in range(len(minerals) // 5 + 1)]
    
    for i in range(len(minerals)):
        if minerals[i] == 'diamond':
            mineral_count[i // 5][0] += 1
            
        elif minerals[i] == 'iron':
            mineral_count[i // 5][1] += 1
            
        elif minerals[i] == 'stone':
            mineral_count[i // 5][2] += 1
    
    mineral_count.sort(key = lambda x : (-x[0], -x[1], -x[2]))
    answer = 0

    for i in mineral_count:
        dia, iron, stone = i

        for j in range(len(picks)):
            if picks[j] > 0 and j == 0:
                picks[j] -= 1
                answer += dia + iron + stone
                break

            elif picks[j] > 0 and j == 1 :
                picks[j] -= 1
                answer += 5 * dia + iron + stone
                break
            
            elif picks[j] > 0 and j == 2:
                picks[j] -= 1
                answer += 25 * dia + 5 * iron + stone
                break
    print(answer)

solution([0, 1, 1], ["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"])