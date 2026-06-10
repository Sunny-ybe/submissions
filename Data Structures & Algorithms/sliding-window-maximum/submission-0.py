class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0 
        r = l + k
        res = []
        m = nums[0]

        while r < len(nums)+1:
            s = set(nums[l:r])
            m = max(s)
            if m < max(s):
                m = max(s)
            res.append(m)
            l+=1
            r+=1

        return res
            
            

            