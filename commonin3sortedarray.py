class Solution:
    def commonElements(self, arr1, arr2, arr3):
        #Code Here
        i = j = k = 0
        n1, n2, n3 = len(arr1), len(arr2), len(arr3)
        res = []
        
        while i < n1 and j < n2 and k < n3:
            
            # if all equal → common element
            if arr1[i] == arr2[j] == arr3[k]:
                # avoid duplicates in result
                if not res or res[-1] != arr1[i]:
                    res.append(arr1[i])
                i += 1
                j += 1
                k += 1
            
            # move pointer of smallest element
            elif arr1[i] < arr2[j]:
                i += 1
            elif arr2[j] < arr3[k]:
                j += 1
            else:
                k += 1
        
        # GFG expects [-1] if empty
        return res if res else [-1]
