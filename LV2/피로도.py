from itertools import permutations

def solution(k, dungeons):

    answer = 0
    dun_len = len(dungeons)

    for permute in permutations(dungeons, dun_len):
        hp = k
        count = 0

        for i in permute:
            if hp >= i[0]:
                hp -= i[1]
                count += 1

            else:
                break 
            
        answer = max(answer, count)
            
    return answer

solution(80, [[80,20],[50,40],[30,10]])