class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        result = 0
        levels = defaultdict(list)

        # extract values per level
        def deeper(node, depth):
            if node:
                levels[depth].append(node.val)
                deeper(node.left,  depth + 1)
                deeper(node.right, depth + 1)

        deeper(root, 0)
        for l in levels.values():
            size = len(l)
            # find final position of each entries
            pos  = sorted(range(size), key = lambda x : l[x])
            for i in range(size):
                # swap until correct position found
                while pos[i] != i:
                    result += 1
                    other   = pos[i]
                    pos[i], pos[other] = pos[other], pos[i]

        return result
