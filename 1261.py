class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        self.all = set()
        self.add(root, 0)

    def add(self, node, id): # convert to hashed set
        if node:
            self.all.add(id)
            self.add(node.left,  2 * id + 1)
            self.add(node.right, 2 * id + 2)

    def find(self, target: int) -> bool:
        return target in self.all
