class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        # similiar to problem 102
        levels = defaultdict(list)

        def deeper(node, depth):
            if node:
                levels[depth].append(node.val)
                deeper(node.left,  depth+1)
                deeper(node.right, depth+1)

        deeper(root, 0)

        return reversed([ levels[l] for l in sorted(levels.keys()) ])
