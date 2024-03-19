def solution(arr1, arr2):
    answer = []
    
    for i in range(len(arr1)):
        arr = []
        for k in range(len(arr2[0])):
            temp = 0
            for j in range(len(arr1[0])):
                temp += arr1[i][j] * arr2[j][k]
            arr.append(temp)
        answer.append(arr)      
            
    return answer
