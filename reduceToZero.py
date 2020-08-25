def reduceToZero(num: int) -> int:
    iterations = 0
    
    while num != 0:
        if num % 2 == 0:
            iterations += 1
            num /= 2
        else:
            iterations += 1
            num -= 1
    return iterations

print(reduceToZero(13))
print(reduceToZero(14))
print(reduceToZero(2000))