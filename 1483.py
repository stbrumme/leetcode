class TreeAncestor:
    def __init__(self, n: int, parent: List[int]):
        # powers of ten
        steps = [ 1, 10, 100, 1_000, 10_000 ]
        self.parents = { 1: parent, 10: [], 100: [], 1_000: [], 10_000: [] }

        # 10th/100th parent
        for s in steps[1:]:
            for i in range(n):
                x = i
                # based on the previous step size
                for i in range(10):
                    if x != -1:
                        x = self.parents[s // 10][x]

                self.parents[s].append(x)

    def getKthAncestor(self, node: int, k: int) -> int:
        x = node

        for s in reversed(self.parents):
            while k >= s:
                x = self.parents[s][x]
                if x == -1:
                    return -1
                k -= s

        return x

# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)
