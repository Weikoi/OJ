# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        # elif abs(self.max_depth(root.left) - self.max_depth(root.right)) > 1:
        # elif abs(self.max_depth(root.left) - self.max_depth(root.left)) > 1:
        # return False
        # else:
        #     return self.isBalanced(root.left) and self.isBalanced(root.right)

        elif abs(self.max_depth(root.left) - self.max_depth(root.left)) > 1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)

    def max_depth(self, tree):
        """
        :param tree:
        :return depth of tree:
        """
        if not tree:
            return 0
        else:
            return max(self.max_depth(tree.right) + 1, self.max_depth(tree.left) + 1)
