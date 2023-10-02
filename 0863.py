class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        edges = defaultdict(set)

        # find all edges
        def deeper(node, parentVal):
            if not node:
                return

            if parentVal is not None:
                edges[node.val ].add(parentVal)
                edges[parentVal].add(node.val)

            deeper(node.left,  node.val)
            deeper(node.right, node.val)

        deeper(root, None)

        # basic BFS
        todo = set([ target.val ])
        have = set()
        for steps in range(k):
            next = set()
            for t in todo:
                have.add(t)
                next |= edges[t] - have

            todo = next

        return list(todo)
