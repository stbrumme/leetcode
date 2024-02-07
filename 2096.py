class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        # path from node to value or None if not found
        def deeper(node, value):
            if not node:
                return None

            if node.val == value:
                return ""

            left  = deeper(node.left,  value)
            if left != None:
                return "L" + left

            right = deeper(node.right, value)
            if right != None:
                return "R" + right

            return None

        # full path from root
        one = deeper(root, startValue)
        two = deeper(root, destValue)

        # find common path
        same = 0
        for o, t in zip(one, two):
            if o != t:
                break
            same += 1

        # replace first path by "U"
        return "U" * (len(one) - same) + two[same :]
