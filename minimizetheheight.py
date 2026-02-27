n = len(arr)
        arr.sort()
        
        ans = arr[-1] - arr[0]   # initial difference
        
        small = arr[0] + k
        big = arr[-1] - k
        
        if small > big:
            small, big = big, small
        
        for i in range(1, n-1):
            subtract = arr[i] - k
            add = arr[i] + k
            
            # skip if no effect on min/max
            if subtract >= small or add <= big:
                continue
            
            # update min or max
            if big - subtract <= add - small:
                small = subtract
            else:
                big = add
        
        return min(ans, big - small)
