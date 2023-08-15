class Solution:
    def deeper(self, root, sumSoFar, target):
        if not root:
            return None

        sumSoFar += root.val

        if not root.left and not root.right:
            if sumSoFar == target:
                return [ [ root.val ] ]
            else:
                return None

        result = []
        paths = self.deeper(root.left, sumSoFar, target)
        if paths:
            for p in paths:
                result.append([ root.val ] + p)
        paths = self.deeper(root.right, sumSoFar, target)
        if paths:
            for p in paths:
                result.append([ root.val ] + p)

        return result


    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []

        return self.deeper(root, 0, targetSum)
