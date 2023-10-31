class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        # use binary search in an array

        all = []
        def flatten(node):
            if node:
                all.append(node.val)
                flatten(node.left)
                flatten(node.right)

        flatten(root)
        all.sort()

        for q in queries:
            left  = bisect_right(all, q)
            right = bisect_left (all, q)
            yield [ all[left - 1] if left > 0 else -1, all[right] if right < len(all) else -1 ]
