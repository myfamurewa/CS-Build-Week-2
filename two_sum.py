def twoSum(arr: list, targetSum: int) -> list:
    arr.sort()
    left = 0
    right = len(arr) - 1

    while(left < right) :
        currentSum = arr[left] + arr[right]
        if currentSum == targetSum:
            return [left, right]
        elif currentSum < targetSum:
            left += 1
        elif currentSum > targetSum:
            right -= 1

    return []
    

def twoSumV2(arr: list, targetSum: int) -> list:
    twoSum = []
    for i in range(len(arr)):
        if arr.count(targetSum - arr[i]) == 1 and arr.index(targetSum - arr[i]) != i and len(twoSum) < 2:
            twoSum = [i, arr.index(targetSum - arr[i])]
    return twoSum


