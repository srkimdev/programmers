def solution(n):
    a = bin(n)[2:]
    count_a = a.count('1')
    
    while True:
        n += 1
        
        b = bin(n)[2:]
        count_b = b.count('1')
        
        if count_a == count_b:
            break
    
    return n