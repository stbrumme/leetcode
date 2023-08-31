class Solution:
    def connect(self, root: 'Node') -> 'Node':
        rightmost = { }

        def deeper(node, depth):
            if not node:
                return

            if depth in rightmost:
                node.next = rightmost[depth]
            rightmost[depth] = node

            # order is important !
            deeper(node.right, depth+1)
            deeper(node.left,  depth+1)

        deeper(root, 0)
        return root
