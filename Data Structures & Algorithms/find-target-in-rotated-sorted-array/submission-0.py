class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] == target:
                return mid
            
            #left side is sorted
            if nums[l] <= nums[mid]:
                if nums[l] <= target <= nums[mid]:
                    r = mid
                else:
                    l = mid + 1

            #right side is sorted
            elif nums[l] >= nums[mid]:
                if nums[mid] <= target <= nums[r]:
                    l = mid
                else:
                    r = mid

            
        return -1

        

        
        