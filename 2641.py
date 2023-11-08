class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        levels = defaultdict(int)
        def levelsum(node, depth):
            if node:
                levels[depth] += node.val

                levelsum(node.left,  depth + 1)
                levelsum(node.right, depth + 1)

        def update(node, cousin, depth):
            if node:
                node.val = levels[depth] - (node.val + cousin)
                # children's cousins
                l = node.left.val  if node.left  else 0
                r = node.right.val if node.right else 0

                update(node.left,  r, depth + 1)
                update(node.right, l, depth + 1)

        levelsum(root, 0)
        update  (root, 0, 0)
        return root
