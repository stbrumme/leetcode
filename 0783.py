class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        all = []
        def deeper(node):
            if node:
                all.append(node.val)
                deeper(node.left)
                deeper(node.right)

        deeper(root)

        all.sort()
        best = all[1] - all[0]
        for i in range(2, len(all)):
            best = min(best, all[i] - all[i - 1])
        return best
