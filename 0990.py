class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        # union-find, copied from problem 721
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x]) # path compression
            return parent[x]

        def union(x, y):
            x = find(x)
            y = find(y)
            if x == y:
                return
            if x < y:
                parent[y] = x
            else:
                parent[x] = y

        # find all variables in use
        parent = {}
        for e in equations:
            left  = e[0]
            right = e[3]
            parent[left ] = left
            parent[right] = right

        # identical variables
        for e in equations:
            compare = e[1:3]
            if compare == "==":
                left  = e[0]
                right = e[3]
                union(left, right)

        # negated variables must not have the same parent
        for e in equations:
            compare = e[1:3]
            if compare == "!=":
                left  = e[0]
                right = e[3]
                if find(left) == find(right):
                    return False

        return True
