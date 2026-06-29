class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # for i in range(len(nums)):
        #     if nums[abs(nums[i]) - 1] < 0:
        #         return abs(nums[i])
        #     nums[abs(nums[i]) - 1] *= -1

        slow = 0
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0

        while True:
            slow = nums[slow]
            slow2=nums[slow2]
            if slow2==slow:
                return slow2


            


            


        



        