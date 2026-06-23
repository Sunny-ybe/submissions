class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        m = max(piles)
        if len(piles) == h:
            return m

        def canfinish(k):
            hours = 0
            for p in piles:
                hours += (p + k-1) // k
           
            return hours <= h
        
        l = 1
        r = m
        while l < r:
            mid = (l+r) // 2
            if canfinish(mid):
                r = mid
            else:
                l = mid+1
        return l
            




