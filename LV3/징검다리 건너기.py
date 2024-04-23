#7:15
# def solution(stones, k):
#     count = 0
#     temp = 0

#     while temp < k:
#         temp = 0 # 연속으로 못건넌 횟수 저장

#         for i in range(len(stones)):
#             if temp == k:
#                 break

#             if stones[i] >= 1:
#                 stones[i] -= 1
#                 temp = 0
#             else:
#                 temp += 1
                
#         if temp == k:
#             break
#         else:
#             count += 1

#     return count

def solution(stones, k):

    start = 1
    end = max(stones)
    result = 0

    while start <= end:
        temp = 0 # mid 이하의 돌의 개수
        mid = (start + end) // 2

        for stone in stones:
            if stone <= mid:
                temp += 1

            else:
                temp = 0

            if temp >= k:
                break

        if temp < k:
            start = mid + 1

        else:
            end = mid - 1
            result = mid

    return result

solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3)