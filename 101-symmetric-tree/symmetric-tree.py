class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        left_list = []
        right_list = []
        
        def rec_left(node):
            if node is None:
                left_list.append(None)
                return
            left_list.append(node.val)
            rec_left(node.left)
            rec_left(node.right)
        
        def rec_right(node):
            if node is None:
                right_list.append(None)
                return
            right_list.append(node.val)
            rec_right(node.right)
            rec_right(node.left)
        
        rec_left(root.left)
        rec_right(root.right)
        
        if left_list == right_list:
            return True
        else:
            return False