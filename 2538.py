class Solution:
    def maxOutput(self, n: int, edges: List[List[int]], price: List[int]) -> int:
        result = 0

        # build graph
        next = [ [] for _ in range(n) ]
        for a, b in edges:
            next[a].append(b)
            next[b].append(a)

        def deeper(node, previous):
            high = price[node]
            low  = 0
            for other in next[node]:
                # avoid loops
                if other == previous:
                    continue

                # search to the end
                highMore, lowMore = deeper(other, node)

                # assume current node is the optimal root
                nonlocal result
                result = max(result, highMore + low, high + lowMore)

                # update range
                high = max(high, price[node] + highMore)
                low  = max(low,  price[node] + lowMore)

            return high, low

        deeper(0, 0)
        return result
