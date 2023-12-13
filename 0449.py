class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        tokens = []
        def deeper(node):
            nonlocal tokens
            if node:
                # preorder
                tokens.append(str(node.val))
                deeper(node.left)
                deeper(node.right)
            else:
                tokens.append("")

        deeper(root)
        return "|".join(tokens)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        tokens = data.split("|")
        pos    = 0

        def deeper():
            nonlocal pos, tokens
            value = tokens[pos]
            pos  += 1

            if value == "":
                return None
            else:
                left  = deeper()
                right = deeper()
            return TreeNode(int(value), left, right)

        return deeper()
