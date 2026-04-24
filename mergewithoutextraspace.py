import math
class Solution:
    def mergeArrays(self, a, b):
        # code here
        n = len(a)
        m = len(b)
        
        # Initial gap
        gap = math.ceil((n + m) / 2)
        
        while gap > 0:
            i = 0
            j = gap
            
            while j < (n + m):
                # Case 1: both pointers in array a
                if i < n and j < n:
                    if a[i] > a[j]:
                        a[i], a[j] = a[j], a[i]
                
                # Case 2: i in a, j in b
                elif i < n and j >= n:
                    if a[i] > b[j - n]:
                        a[i], b[j - n] = b[j - n], a[i]
                
                # Case 3: both in b
                else:
                    if b[i - n] > b[j - n]:
                        b[i - n], b[j - n] = b[j - n], b[i - n]
                
                i += 1
                j += 1
            
            # Reduce gap
            if gap == 1:
                gap = 0
            else:
                gap = math.ceil(gap / 2)
    
            
            
        # code here
        
        
