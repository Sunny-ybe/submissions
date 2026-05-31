class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # seen = set() 
        # for i in range(len(nums)):
        #     if nums[i] not in seen:
        #         seen.add(nums[i])
        #     else:
        #         seen.remove(nums[i])
        # lst = list(seen)
        # return lst[0]
        #using Bitwise operator
        result = 0
        for n in nums:
            result ^= n
        return result
        