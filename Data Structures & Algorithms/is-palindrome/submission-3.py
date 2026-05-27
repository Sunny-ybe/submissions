class Solution:
    def isPalindrome(self, s: str) -> bool:
        #s_cleaned = "".join(ch.lower() for ch in s if ch.isalnum())
        # s_rev = s_cleaned[::-1]
        # n = len(s_rev)
        # for i in range(n):
        #     if s_rev[i] != s_cleaned[i]:
        #         return False
        # return True
        #more efficient algo below
        # n = len(s_cleaned)
        # for i in range(n//2):
        #     if s_cleaned[i] != s_cleaned[n-1-i]:
        #         return False
        # return True 
    #Two Pointer Algo
        left, right = 0, len(s)-1

        while left < right:
            while left < right and not self.alphanumeric(s[left]):
                left +=1
            while right > left and not self.alphanumeric(s[right]):
                right-=1
            if s[left].lower() != s[right].lower():
                return False
            left, right = left+1, right-1
        return True



    def alphanumeric(self,c)-> bool:
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))

        




        