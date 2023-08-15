class Solution:
    stacks = { }

    def inorder(self, root, depth = 0):
        if not root:
            return None

        prev = self.stacks.get(depth)
        if prev:
            prev.next = root
        self.stacks[depth] = root

        self.inorder(root.left,  depth + 1)
        self.inorder(root.right, depth + 1)


    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        self.inorder(root)
        return root
