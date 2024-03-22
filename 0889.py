class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        pre  = 0
        post = 0

        def deeper():
            nonlocal pre, post

            # root node is always the left-most element
            root = TreeNode(preorder[pre])
            pre += 1

            # left  subtree
            if root.val != postorder[post]:
                root.left  = deeper()
            # right subtree
            if root.val != postorder[post]:
                root.right = deeper()

            post += 1
            return root

        return deeper()
