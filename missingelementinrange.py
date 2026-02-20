class Solution:
    def missingRange(self, arr, low, high):
        #code here
        res=[]
        s=set(arr)
        
        for  i in range (low,high+1):
            
            if i not in s:
                res.append(i)
        return res
