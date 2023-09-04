class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        @cache
        def serialize(node):
            if node:
                return "l=" + serialize(node.left) + "|" + str(node.val) + "|r=" + serialize(node.right)
            else:
                return ""

        lookfor = serialize(subRoot)
        result  = False

        def deeper(node):
            if node:
                nonlocal lookfor, result
                if serialize(node) == lookfor:
                    result = True
                    return

                deeper(node.left)
                deeper(node.right)

        deeper(root)
        return result
