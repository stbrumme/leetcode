class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        all = []
        def deeper(node):
            if node:
                deeper(node.left)
                all.append(node)
                deeper(node.right)
        deeper(root)

        for i in range(len(all)):
            all[i].left = None
            if i < len(all) - 1:
                all[i].right = all[i + 1]

        return all[0]
