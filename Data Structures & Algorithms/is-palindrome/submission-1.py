class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_cleaned = "".join(ch.lower() for ch in s if ch.isalnum())
        # s_rev = s_cleaned[::-1]
        # n = len(s_rev)
        # for i in range(n):
        #     if s_rev[i] != s_cleaned[i]:
        #         return False
        # return True
        #more efficient algo below
        n = len(s_cleaned)
        for i in range(n//2):
            if s_cleaned[i] != s_cleaned[n-1-i]:
                return False
        return True 




        