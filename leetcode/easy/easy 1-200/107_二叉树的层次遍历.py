# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    @staticmethod
    def levelOrderBottom(root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = [root]
        value_list = []
        while queue:
            temp_value_list =[]
            for i in range(len(queue)):
                cur = queue.pop(0)
                temp_value_list.append(cur.val)
                if cur.right:
                    queue.append(cur.right)
                if cur.left:
                    queue.append(cur.left)
            value_list.append(temp_value_list)


