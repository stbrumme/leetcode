class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        all = defaultdict(list)
        for a, b in edges:
            all[a].append(b)
            all[b].append(a)

        restricted = set(restricted) # faster access than list

        def deeper(node, previous):  # avoid loops by comparing against previous node
            result = 1               # current node
            for a in all[node]:      # all children
                if a != previous and a not in restricted:
                    result += deeper(a, node)
            return result

        return deeper(0, -1)
