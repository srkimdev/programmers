def solution(s):
    answer = []
    zero, count = 0, 0

    while s != '1':
        for i in s:
            if i == '0':
                zero += 1
        s = s.replace('0', '')

        s = bin(len(s))
        s = s[2:]
        count += 1

    return [count, zero]