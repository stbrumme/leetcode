class CBTInserter:
    def __init__(self, root: Optional[TreeNode]):
        self.root  = root
        self.nodes = defaultdict(list) # all nodes, partitioned by their depth
        self.pos   = defaultdict(int)  # first node per depth which is incomplete

        def deeper(node, depth):
            if node:
                have = 0
                if node.left:
                    deeper(node.left,  depth + 1)
                    have += 1
                if node.right:
                    deeper(node.right, depth + 1)
                    have += 1

                # move single children to the left side
                if have == 1 and node.right:
                    node.left  = node.right
                    node.right = None

                self.nodes[depth].append(node)
                # skip complete nodes
                if have == 2:
                    self.pos[depth] += 1

        deeper(root, 0)

    def insert(self, val: int) -> int:
        # determine depth of the parent node
        depth = 0
        while self.pos[depth] == len(self.nodes[depth]):
            depth += 1 # skip full layers

        # create new node
        add = TreeNode(val)
        self.nodes[depth + 1].append(add)

        # and connect it to its parent
        available = self.pos[depth]
        parent    = self.nodes[depth][available]
        if parent.left:
            parent.right = add
            # parent node is complete
            self.pos[depth] += 1
        else:
            parent.left  = add

        return parent.val

    def get_root(self) -> Optional[TreeNode]:
        return self.root
