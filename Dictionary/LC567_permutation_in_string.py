from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str):
        if len(s1)> len(s2):
            return False
        
        s1_count = Counter(s1)
        window = Counter()
        
        left = 0
        
        for right in range(len(s2)):
            window[s2[right]]+=1
            
            if right-left+1>len(s1):
                del window[s2[left]]
                left += 1
            
            if window == s1_count:
                return True
        
        return False