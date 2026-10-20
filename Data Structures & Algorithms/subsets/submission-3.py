class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        out = [[]]
        for num in nums:
            subsets = out.copy()
            for s in subsets:
                out.append(s+[num])
        return out




        