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
