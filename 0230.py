class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inorder = []

        def deeper(node):
            if node and len(inorder) < k: # early exit if k is small
                deeper(node.left)
                inorder.append(node.val)
                deeper(node.right)

        deeper(root)
        return inorder[k - 1] # zero-based
