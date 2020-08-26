# Understand
# In Pascal's triangle, each number is the sum of the two numbers directly above it
'''
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

'''
# Plan
# We need to return a list of lists
# the first element in the list is always one
# each subsequent level has one more element than the previous level
# The first and last element in each list will always be one
# The inner elements are calculated by adding the number index of the number in the previous row and the index of the number minus one in the previous row
# 
# 
# for the rows the value is the  



class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rows = []
        for i in range(numRows):
            if i == 0:
                rows.append([1])
            elif i == 1:
                rows.append([1,1])
            else:
                new_row = [1]
                middle_number_count = i - 1
                
                for j in range(middle_number_count):
                    col_index = j + 1
                    prev_row = rows[-1]
                    value = prev_row[col_index] + prev_row[col_index - 1]
                    new_row.append(value)
                new_row.append(1)
                rows.append(new_row)
        return rows
