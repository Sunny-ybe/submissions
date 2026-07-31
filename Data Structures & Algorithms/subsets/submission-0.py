class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        res.append([])
        for i in range(len(nums)):
            index = len(res)
            for subset in res[:index]:
                copy = subset.copy()
                copy.append(nums[i])
                res.append(copy)
        return res
            

            



        
        