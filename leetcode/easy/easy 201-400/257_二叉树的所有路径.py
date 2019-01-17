class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root is None:
            return []

        if root.left is None and root.right is None:
            return [str(root.val)]

        Paths = self.binaryTreePaths(root.left) + self.binaryTreePaths(root.right)

        for index in range(len(Paths)):
            Paths[index] = str(root.val) + "->" + Paths[index]

        return Paths
