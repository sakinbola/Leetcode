# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):

        def invert(root):
            if not root:
                return 
            
            root.left , root.right = root.right , root.left
            
            invert(root.left)
            invert(root.right)

            return root
        
        return invert(root)
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        