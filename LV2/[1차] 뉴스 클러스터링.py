def solution(str1, str2):
    answer = 0
    list1 = []
    list2 = []
    hap, gyo = 0, 0
    
    for i in range(len(str1) - 1):
        temp = str1[i] + str1[i + 1]
        
        if temp.isalpha():
            list1.append(temp.lower())
    len_list1 = len(list1)

    for i in range(len(str2) - 1):
        temp = str2[i] + str2[i + 1]

        if temp.isalpha():
            list2.append(temp.lower())
    len_list2 = len(list2)

    while list1:
        a = list1.pop(0)

        for i, v in enumerate(list2):
            if a == v:
                gyo += 1
                list2.pop(i)
                break

    hap = len_list1 + len_list2 - gyo
    
    if hap == gyo == 0:
        return 65536
    answer = int(gyo / hap * 65536)

    return answer
