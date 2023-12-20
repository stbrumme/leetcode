class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        pos = 0

        def deeper(stop): # "stop" indicates that no value in the subtree should be larger than it
            nonlocal pos
            if pos == len(preorder):
                return None

            value = preorder[pos]
            if value > stop:
                return None

            node = TreeNode(value)
            pos += 1
            node.left  = deeper(value)
            node.right = deeper(stop)
            return node

        return deeper(+inf)
