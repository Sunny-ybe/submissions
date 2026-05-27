class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_cleaned = "".join(ch.lower() for ch in s if ch.isalnum())
        s_rev = s_cleaned[::-1]
        n = len(s_rev)
        for i in range(n):
            if s_rev[i] != s_cleaned[i]:
                return False
        return True



        