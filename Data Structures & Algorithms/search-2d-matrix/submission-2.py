class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # for i in range(len(matrix)):
        #     if matrix[i][0] <= target and matrix[i][-1] >= target:
        #         for num in matrix[i]:
        #             if num == target:
        #                 return True

        # return False     better than brute force but O(m + n)
        #                  can be done in O(log(m*n))

        l = 0
        m = len(matrix)
        n = len(matrix[0])
        r = m*n - 1

        while l <= r:
            mid = (l+r) //2
            row = mid // n
            col = mid % n
            if target == matrix[row][col]:
                return True
            elif target > matrix[row][col]:
                l = mid + 1
            else:
                r = mid - 1
        return False
            
        
        



                


        
        
            



