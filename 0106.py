class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # almost the same as problem 105
        def parse(post, inn):
            if not inn:
                return None

            value = post[-1]
            node = TreeNode(value)
            if len(inn) == 1:
                return node

            pos = inn.index(value)

            inn_left  = inn[:pos]
            inn_right = inn[pos+1:]
            inn_left_faster = frozenset(inn_left)
            post_left  = []
            post_right = []
            for p in post[:-1]:
                if p in inn_left_faster:
                    post_left.append(p)
                else:
                    post_right.append(p)

            node.left  = parse(post_left,  inn_left)
            node.right = parse(post_right, inn_right)
            return node

        return parse(postorder, inorder)
