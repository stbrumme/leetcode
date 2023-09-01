class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        # see 589
        def deeper(node):
            if node:
                for i in node.children:
                    yield from deeper(i)
                yield node.val

        return deeper(root)
