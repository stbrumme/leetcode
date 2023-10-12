class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        nodes = preorder.split(",")
        pos   = 0
        def deeper():
            nonlocal pos
            if pos == len(nodes): # not enough nodes
                return False

            current = nodes[pos]
            pos    += 1
            if current == "#":    # leaf
                return True

            return deeper() and deeper() # process left and right children

        return deeper() and pos == len(nodes) # must be a complete tree and nothing left in the string
