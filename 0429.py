class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        levels = defaultdict(list)

        def deeper(node, depth):
            if node:
                levels[depth].append(node.val)
                for i in node.children:
                    deeper(i, depth + 1)

        deeper(root, 0)

        for i in levels:
            yield levels[i]
