"""
只要符合左小于根节点小于右，那么他们的最小公共就是根节点，然后再递归

"""


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if q.val >= root.val >= p.val or q.val <= root.val <= p.val:
            return root
        elif q.val > root.val and p.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif q.val < root.val and p.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return None
