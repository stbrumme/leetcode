class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        leafs = []
        def deeper(node, have):
            if node:
                have <<= 1
                have  += node.val
                if node.left or node.right:
                    deeper(node.left,  have)
                    deeper(node.right, have)
                else:
                    leafs.append(have)

        deeper(root, 0)
        return sum(leafs)
