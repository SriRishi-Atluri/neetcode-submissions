class Solution:
    def isPalindrome(self, s: str) -> bool:
        fixed_string = s.lower()
        palindrome_string = ""

        for c in fixed_string:
            if c.isalnum():
                palindrome_string += c

        return palindrome_string == palindrome_string[::-1]
