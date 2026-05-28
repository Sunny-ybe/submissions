class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        c = 0
        m = 0

        for n in nums:
            if n-1 in s:
                continue
            i = 1
            c=1
            while n+i in s:
                if n+i in s:
                    c+=1
                i+=1
            m = max(c,m)
        return m

            
            
            





