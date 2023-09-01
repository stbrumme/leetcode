class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        def deeper(node):
            if node:
                yield node.val
                for i in node.children:
                    yield from deeper(i)

        return deeper(root)
