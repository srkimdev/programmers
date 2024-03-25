def solution(elements):
    answer = 0
    temp = []
    len_ele = len(elements)
    elements = elements + elements

    for i in range(1, len_ele + 1): # 몇번 더할지
        for j in range(len_ele): # 시작위치
            temp.append(sum(elements[j:j + i]))

    temp = list(set(temp))

    return len(temp)
