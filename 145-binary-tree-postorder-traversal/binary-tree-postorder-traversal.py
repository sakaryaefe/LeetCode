# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        list = []
        def rec(node):
            if node is None:
                return
            rec(node.left)
            rec(node.right)
            list.append(node.val)
        rec(root)
        return list

        