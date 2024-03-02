def solution(n, words):
    turn = 1
    s = words[0][-1] #단어의 끝 저장
    temp = [words[0]]

    for i in range(1, len(words)):
        if len(temp) % n == 0:
            turn += 1
        if s == words[i][0] and words[i] not in temp:
            s = words[i][-1]
            temp.append(words[i])
        else:
            return i % n + 1, turn
    
    if len(temp) == len(words):
        return [0, 0]