# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
    # max in path not global max 
        # if not root:
        #     return 0

        # count = 1

        # q = collections.deque([root])
        # mmax = root.val
        # while q:
        #     qlen = len(q)
            
        #     for i in range(qlen):
        #         node = q.popleft()
        #         if node:
        #             if node.val > mmax:
        #                 count+=1
        #             q.append(node.left)
        #             q.append(node.right)

        #         if node:
        #             mmax = max(node.val, mmax)
        # return count - wrong because i did max global smh fuck me 

        if not root:
            return 0
        count = 0

        q = collections.deque([(root, root.val)])

        while q:
            node, pathmax = q.popleft()

            if node.val >= pathmax:
                count+=1
            
            newmax = max(pathmax,node.val)

            if node.left:
                q.append((node.left, newmax))
            if node.right:
                q.append((node.right, newmax))
            
        return count





        