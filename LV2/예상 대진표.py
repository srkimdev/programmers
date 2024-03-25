def solution(n,a,b):
    answer = 0

    start = 1
    end = n

    a = min(a, b)
    b = max(a, b)

    while start <= end:
        mid = (start + end) // 2

        if a <= mid and b > mid:
            

    

    return answer