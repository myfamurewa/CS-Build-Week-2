import math

def isPowerOfFour(num: int) -> bool:
    if num < 0 or num == 0:
        return False
    print(num, math.pow(num , 1/4))
    return math.sqrt(math.sqrt(num)).is_integer()

print(isPowerOfFour(64))
