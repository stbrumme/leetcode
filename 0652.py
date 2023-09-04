class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        @cache # from problem 572
        def serialize(node):
            if node:
                return "l=" + serialize(node.left) + "|" + str(node.val) + "|r=" + serialize(node.right)
            else:
                return ""

        all = defaultdict(int)
        def deeper(node):
            if node:
                s = serialize(node)
                all[s] += 1
                if all[s] == 2: # emit second tree's root node
                    yield node

                yield from deeper(node.left)
                yield from deeper(node.right)

        yield from deeper(root)
