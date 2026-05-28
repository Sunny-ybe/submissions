class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0, len(height)-1
        res = 0
        leftmax,rightmax = 0,0
        while l < r:
            leftmax = max(leftmax,height[l])
            rightmax = max(height[r],rightmax)
            if leftmax < rightmax:
                res += leftmax - height[l]
                l+=1
            else:
                res += rightmax - height[r]
                r-=1
        return res
                
                



        