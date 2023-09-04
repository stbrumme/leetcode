class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        result = 0
        def deeper(node):
            if not node:
                return []

            paths = [ [ node.val ] ]
            for p in deeper(node.left):
                paths.append(p + [ node.val ])
            for p in deeper(node.right):
                paths.append(p + [ node.val ])

            for p in paths:
                if sum(p) == targetSum:
                    nonlocal result
                    result += 1
            return paths

        deeper(root)
        return result
