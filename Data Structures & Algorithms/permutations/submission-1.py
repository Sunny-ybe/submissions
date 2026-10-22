class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # res = []
        # choosen = [False]*len(nums)

        # def dfs(curr):
        #     if len(curr) == len(nums):
        #         res.append(curr.copy())
        #     for j in range(len(nums)):
        #         if choosen[j]:
        #             continue
        #         choosen[j] = True
        #         curr.append(nums[j])
        #         dfs(curr)
        #         curr.pop()
        #         choosen[j] = False   
        # dfs([])
        # return res


        res = []
        choosen = [False]*len(nums)
        
        def dfs(curr):
            if len(nums) ==1:
                return res.append(nums)
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            
            if len(curr) > len(nums):
                return
            
            for i in range(len(nums)):
                if choosen[i]:
                    continue
                choosen[i] = True
                curr.append(nums[i])
                
                dfs(curr)
                curr.pop()
                choosen[i] = False
                

        dfs([])
        return res

            





















        
        