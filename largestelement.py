class Solution:
    def largest(self, arr):
        # code here
        n=len(arr)
        arr.sort()
        return arr[n-1]
        
