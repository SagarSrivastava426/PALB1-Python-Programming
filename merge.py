class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged=[]
        for i in intervals:
            if not merged or merged[-1][1]<i[0]:
                merged.append(i[:])
            else:
                if i[1]>merged[-1][1]:
                    merged[-1][1]=i[1]
        return merged


        
        
