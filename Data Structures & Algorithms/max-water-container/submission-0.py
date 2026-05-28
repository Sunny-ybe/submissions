class Solution:
    def maxArea(self, heights: List[int]) -> int:
        m = 0
        l,r = 0, len(heights)-1
        while l < r :
            area = min(heights[l],heights[r])*abs(l-r)
            if area > m:
                m=area
            if heights[l] < heights[r]:
                l+=1
            elif heights[l] > heights[r]:
                r-=1
            elif heights[l] == heights[r]:
                l+=1
                r-=1
        return m
        