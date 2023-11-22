class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        flat = []
        # in-order walk
        def flatten(node):
            if node:
                flatten(node.left)
                flat.append(node.val)
                flatten(node.right)

        def balance(left, right):
            # invalid range
            if left >  right:
                return None
            # leaf
            if left == right:
                return TreeNode(flat[left])

            # for performance reasons: let's process these easy cases explicitly
            if left == right + 1:
                return TreeNode(flat[left], None, TreeNode(flat[right]))
            if left == right + 2:
                return TreeNode(flat[left + 1], TreeNode(flat[left]), TreeNode(flat[right]))

            # general case (can handle the two cases above as well)
            mid = (left + right) // 2
            return TreeNode(flat[mid], balance(left,  mid - 1), \
                                       balance(mid + 1, right))

        flatten(root)
        return balance(0, len(flat) - 1)
