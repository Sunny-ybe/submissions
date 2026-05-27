class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        has_0 = False
        prod = 1
        zeroCount = 0
        for i in nums:
            if i != 0:
                prod = prod * i
            else:
                has_0 = True
                zeroCount += 1

        if has_0 == True:
            if zeroCount < 2:
                lst = [0 if i !=0 else prod for i in nums]
            if zeroCount >= 2:
                lst = [0 for i in nums]

        if has_0 == False:
            lst = [int(prod/i) for i in nums]
        return lst
        