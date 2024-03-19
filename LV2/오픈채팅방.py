def solution(record):
    answer = []
    dic = {}
    word = ''

    for i in range(len(record)):
        arr = record[i].split()
        if arr[0] == 'Enter':
            dic[arr[1]] = arr[2]
        
        elif arr[0] == 'Change':
            dic[arr[1]] = arr[2]

    for i in range(len(record)):
        arr = record[i].split()
        if arr[0] == 'Enter':
            word = dic[arr[1]] + '님이 들어왔습니다.'

        elif arr[0] == 'Leave':
            word = dic[arr[1]] + '님이 나갔습니다.'
            
        else:
            continue
        answer.append(word)
    return answer