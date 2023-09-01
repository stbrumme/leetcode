class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None

        if root.val in [ p.val, q.val ]:
            return root

        left  = min(p.val, q.val)
        right = max(p.val, q.val)
        if right < root.val:
            return self.lowestCommonAncestor(root.left,  p, q)
        if left  > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

        return root
