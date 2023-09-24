class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def abc(i):
            return chr(i + ord("a"))

        best = abc(26) # larger than a-z
        def deeper(node, have):
            if not node:
                return

            have = abc(node.val) + have
            if not node.left and not node.right:
                nonlocal best
                best = min(best, have)
                return

            deeper(node.left,  have)
            deeper(node.right, have)
        
        deeper(root, "")
        return best