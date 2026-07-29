class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        n = "".join(str(d) for d in digits)
        n = int(n)+1
        return [int(char) for char in str(n)]

        