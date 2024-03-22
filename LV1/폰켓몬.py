def solution(nums):
    answer = 0

    dic = {}
    for i in nums:
        dic[i] = dic.get(i, 0) + 1
    
    if len(nums) / 2 > len(dic):
        return len(dic)
    else:
        return len(nums) / 2
