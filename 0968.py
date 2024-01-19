class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        result = 0

        # constants (return values of deeper())
        unknown   = -1
        monitored =  0
        camera    = +1

        def deeper(node):
            if not node:
                return monitored

            left  = deeper(node.left)
            right = deeper(node.right)

            # must install camera to monitored one (or both) children
            if left == unknown or right == unknown:
                nonlocal result
                result += 1
                return camera

            # node is next to a camera
            if left == camera  or right == camera:
                return monitored

            # left == monitored and right == monitored
            return unknown

        # both children are monitored, but not root itself
        if deeper(root) == unknown:
            result += 1 # install camera

        return result
