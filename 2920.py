class Solution:
    def maximumPoints(self, edges: List[List[int]], coins: List[int], k: int) -> int:
        size  = len(coins)

        # the only thing making this a hard problem is
        # a potentially huge recursion depth:
        # a linear tree with depth=100 leads to 2^100 calls of deeper()

        # however, the second scoring method aborts pretty early:
        # max(coins) <= 10**4 < 2^15
        # so we have at most about 2^15 + len(coins) calls
        limit = max(coins).bit_length()

        # each node's children
        next  = [ [] for _ in range(size) ]
        for a, b in edges:
            next[a].append(b)
            next[b].append(a)

        # remove parent from next[]
        def tree(node, parent):
            if parent != -1:
                next[node].remove(parent)
            for other in next[node]:
                tree(other, node)

        # start pruning
        tree(0, -1) # -1 = undefined

        @cache
        def deeper(node, shift): # halving is bit shifting
            if shift == limit:
                return 0

            score = coins[node] >> shift

            one = score - k  # first  method: original value minus k
            two = score >> 1 # second method: halved value

            for other in next[node]:
                one += deeper(other, shift)
                two += deeper(other, shift + 1)

            return max(one, two)

        return deeper(0, 0)
