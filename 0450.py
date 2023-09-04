class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        # find node
        if root.val > key:
            root.left  = self.deleteNode(root.left,  key)
            return root
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
            return root

        # one child: skip parent and return the only child
        if not root.left:
            return root.right
        if not root.right:
            return root.left

        # two children, find largest number smaller than key
        up = root
        next = up.left
        while next.right:
            up = next
            next = next.right

        root.val = next.val

        # next has no .right, only .left (which can be None, too)
        if up == root:
            up.left  = next.left
        else:
            up.right = next.left

        return root
