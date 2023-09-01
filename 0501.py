class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        freq = defaultdict(int)

        def deeper(node):
            if node:
                freq[node.val] += 1
                deeper(node.left)
                deeper(node.right)

        deeper(root)
        mode = max(freq.values())
        return [ i for i in freq if freq[i] == mode ]
