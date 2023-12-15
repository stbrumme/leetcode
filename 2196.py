class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        left  = {}
        right = {}
        for parent, child, isleft in descriptions:
            if isleft == 1:
                left [parent] = child
            else:
                right[parent] = child

        # find root's value
        candidates  = set(left) | set(right)
        candidates -= set(left .values())
        candidates -= set(right.values())
        root = min(candidates) # stupid way to retrieve the only element from a set

        def deeper(value):
            node = TreeNode(value)
            if value in left:
                node.left  = deeper(left [value])
            if value in right:
                node.right = deeper(right[value])
            return node

        return deeper(root)
