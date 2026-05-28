class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        c = 0
        m = 0
        for n in nums:
            if n-1 in s:
                continue
            c=1
            while n+c in s:
                c+=1
            m = max(c,m)
        return m

            
            
            





