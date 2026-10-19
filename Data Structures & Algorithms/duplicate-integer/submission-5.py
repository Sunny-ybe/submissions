class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        has_appeared = False
        copy_nums = []
        for i in nums:
            if i not in copy_nums:
                copy_nums.append(i)
            else:
                has_appeared = True
        return has_appeared
        