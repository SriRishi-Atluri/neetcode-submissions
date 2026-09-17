class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)

        if n > m: 
            return False 
        
        need = {}
        for char in s1:
            need[char] = 1 + need.get(char,0)
        
        window  = {}
        for ch in s2[:n]:
            window[ch] = window.get(ch, 0) + 1
        
        if need == window: 
            return True 
        
        for right in range (n,m): 
            ch = s2[right]
            window[ch] = 1 + window.get(ch,0)

            leave = s2[right-n]
            window[leave] -=1 

            if window[leave] == 0: 
                del window[leave]
            
            if window == need: 
                return True 
        
        return False