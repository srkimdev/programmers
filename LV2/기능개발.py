def solution(progresses, speeds):
    answer = []
    
    while progresses:
        count = 0

        while progresses and progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        
        progresses = [progresses[i] + speeds[i] for i in range(len(speeds))]
        
        if count > 0:
            answer.append(count)

    return answer

