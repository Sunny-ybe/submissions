class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        # subsets = set()
        for num in nums:
            subsets = res.copy()
            for subset in subsets:
                res.append(subset+[num])
        return res


        