class Solution:
    def deeper(self, root):
        if not root:
            return []

        current = str(root.val)

        if not root.left and not root.right:
            return [ current ]

        result = []
        for i in self.deeper(root.left):
            result.append(current + i)
        for i in self.deeper(root.right):
            result.append(current + i)

        return result

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        all = self.deeper(root)
        sum = 0
        for i in all:
            sum += int(i)

        return sum
