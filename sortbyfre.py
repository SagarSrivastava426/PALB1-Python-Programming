class Solution:
    def frequencySort(self, s):
        # code here
        
        f={}
        for i in s:
            f[i]=f.get(i,0)+1
        def sort_keys(item):
            return (item[1],item[0])
        ch=sorted(f.items(),key=sort_keys)
        result=[]
        for i ,count in ch:
            result.append(i*count)
            
        return"".join(result)
        
            
            
