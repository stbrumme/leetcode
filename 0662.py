class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = 1
        todo = { 0 : root }

        while todo:
            next = { }
            for pos in todo:
                node = todo[pos]
                if node.left:
                    next[2*pos  ] = node.left
                if node.right:
                    next[2*pos+1] = node.right

            width = 1 + max(todo) - min(todo)
            result = max(result, width)
            todo = next

        return result
