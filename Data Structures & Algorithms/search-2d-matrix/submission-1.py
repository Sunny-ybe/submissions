class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        found = False
        for i in range(len(matrix)):
            if matrix[i][0] <= target and matrix[i][-1] >= target:
                for i in matrix[i]:
                    if i == target:
                        found = True

        return found
