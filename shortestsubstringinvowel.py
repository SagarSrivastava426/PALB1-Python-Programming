class Solution:
    def substrWithVowels(self, s1, s2):
        required = set(s1)
        freq = {}
        
        left = 0
        count = 0
        min_len = float('inf')
        
        for right in range(len(s2)):
            ch = s2[right]
            
            if ch in required:
                freq[ch] = freq.get(ch, 0) + 1
                if freq[ch] == 1:
                    count += 1
            
            # shrink window when all vowels are present
            while count == len(required):
                min_len = min(min_len, right - left + 1)
                
                left_char = s2[left]
                if left_char in required:
                    freq[left_char] -= 1
                    if freq[left_char] == 0:
                        count -= 1
                left += 1
        
        return -1 if min_len == float('inf') else min_len
