class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        flat = set()
        def deeper(node):
            if not node:
                return False

            other = k - node.val
            if other in flat:
                return True

            flat.add(node.val)
            return deeper(node.left) or deeper(node.right)

        return deeper(root)
