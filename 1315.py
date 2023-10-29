class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        result = 0

        def deeper(node, parent, grandparent):
            if node:
                if grandparent % 2 == 0:
                    nonlocal result
                    result += node.val

                deeper(node.left,  node.val, parent)
                deeper(node.right, node.val, parent)

        deeper(root, -1, -1)
        return result
