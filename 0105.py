class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def parse(pree, inn):
            if not inn:
                return None

            value = pree[0]
            node = TreeNode(value)
            if len(inn) == 1:
                return node

            pos = inn.index(value)

            inn_left  = inn[:pos]
            inn_right = inn[pos+1:]
            pree_left  = []
            pree_right = []

            inn_left_faster = set(inn_left)
            for p in pree[1:]:
                if p in inn_left_faster:
                    pree_left.append(p)
                else:
                    pree_right.append(p)

            node.left  = parse(pree_left,  inn_left)
            node.right = parse(pree_right, inn_right)
            return node

        return parse(preorder, inorder)
