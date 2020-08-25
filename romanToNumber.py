def romanToNumber(s: str) -> num:
    romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    #initialize a number
    num = 0

    # convert input to list
    numeralList = list(s)

