class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        # single node
        if n == 1:
            return leftChild == [ -1 ] and rightChild == [ -1 ]

        seen = set()

        def check(i):
            if i == -1:   # terminal node
                return True
            if i >= n:    # referencing an invalid node
                return False

            if i in seen: # don't visit a node twice
                return False
            seen.add(i)

            return check(leftChild[i]) and check(rightChild[i])

        # find root node
        children = set()
        for i in range(n):
            if leftChild[i] != -1:
                children.add(leftChild[i])
            if rightChild[i] != -1:
                children.add(rightChild[i])
        root = -1
        for i in set(range(n)) - children:
            if leftChild[i] != -1 or rightChild[i] != -1:
                if root != -1 and root != i:
                    return False # secondary root
                root = i
        if root == -1:
            return False # no root node at all

        # all nodes should be visited
        return check(root) and len(seen) == n
