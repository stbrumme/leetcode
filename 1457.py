class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def deeper(node, bitmask): # bitmask => set n-th bit if n occurs an odd time
            if not node:
                return 0

            # flip bit
            bitmask ^= 1 << node.val

            # leaf: at most one digit occurs an odd time => at most one bit is set
            if not node.left and not node.right:
                return 1 if bitmask.bit_count() <= 1 else 0

            return deeper(node.left, bitmask) + deeper(node.right, bitmask)

        return deeper(root, 0)
