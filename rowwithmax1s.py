class Solution:
    def rowWithMax1s(self, arr):
        # code here
        max_count = 0
        row_index = -1
    
        for i in range(len(arr)):
            count_ones = sum(arr[i])   # Count number of 1s in the row
            
            if count_ones > max_count:
                max_count = count_ones
                row_index = i
    
        return row_index
