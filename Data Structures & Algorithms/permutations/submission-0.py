class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        choosen = [False]*len(nums)

        def dfs(curr):
            if len(curr) == len(nums):
                res.append(curr.copy())
            for j in range(len(nums)):
                if choosen[j]:
                    continue
                choosen[j] = True
                curr.append(nums[j])
                dfs(curr)
                curr.pop()
                choosen[j] = False   
        dfs([])
        return res
        
        