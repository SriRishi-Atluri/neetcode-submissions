class Solution:
    def isPalindrome(self, s: str) -> bool:
        fixed_string = s.lower().strip()
        new_string = ""

        for c in fixed_string: 
            if c.isalnum(): 
                new_string += c 
        
        return new_string == new_string[::-1]