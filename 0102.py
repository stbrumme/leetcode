class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = defaultdict(list)

        def deeper(node, depth):
            if node:
                levels[depth].append(node.val)
                deeper(node.left,  depth+1)
                deeper(node.right, depth+1)

        deeper(root, 0)
        return [ levels[l] for l in sorted(levels.keys()) ]
