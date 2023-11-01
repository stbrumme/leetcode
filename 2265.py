class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        result = 0

        def deeper(node):
            if not node:
                return 0, 0

            leftcount,  lefttotal  = deeper(node.left)
            rightcount, righttotal = deeper(node.right)

            count = leftcount + rightcount + 1
            total = lefttotal + righttotal + node.val

            avg = total // count
            if avg == node.val:
                nonlocal result
                result += 1

            return count, total

        deeper(root)
        return result
