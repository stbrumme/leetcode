class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        all = []
        def deeper(node):
            if node:
                deeper(node.left)
                deeper(node.right)
                all.append(node.val)

        deeper(root1)
        deeper(root2)
        return sorted(all)
