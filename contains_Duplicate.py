import operator
#Understand
# We are given an array
# if the array contains a duplicate return False
# if it doesn't return true

#Plan
# This problem seems like a perfect situation for a set
# create a new set 
# if the set has the same length as the initial array return true
# else return false

# You could also solve this problem with a dictionary using the same sort of strategy
# every new number is placed in the dictionary with the value as the key and value
# if we encounter a number that is already in the dictionary we return false
# if we get to the end we return True

# Execute
def containsDuplicate(nums: list[int]) -> bool:
    originals = set(nums)
    return operator.not_(len(nums) == len(originals))

def containDuplicate(nums: list[int]) -> bool:
    originals = {}
    for num in nums:
        if num not in originals:
            originals[num] = "True"
        else:
            return True
    
    return False
