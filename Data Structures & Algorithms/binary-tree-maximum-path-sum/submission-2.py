# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # maximum = float("-inf")

        # def dfs(node):
        #     if not node:
        #         return 0
            
        #     nonlocal maximum

        #     left_gain = max(0, dfs(node.left))
        #     right_gain = max(0, dfs(node.right))

        #     current_path = node.val + left_gain + right_gain
        #     maximum = max(maximum, current_path)

        #     return node.val + max(left_gain, right_gain)

        # dfs(root)
        # return maximum



        
        maximum = float("-inf")

        def dfs(node):
            if not node:
                return 0
            
            nonlocal maximum

            left_gain = max(0, dfs(node.left))
            right_gain = max(0, dfs(node.right))

            current_path = node.val + left_gain + right_gain
            maximum = max(maximum, current_path)

            return node.val + max(left_gain, right_gain)

        dfs(root)
        return maximum



















        

        
        