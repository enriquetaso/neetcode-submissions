from string import punctuation

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_format = "".join([c for c in s if c.isalnum()]).lower().replace(" ", "")
        return s_format == s_format[::-1]