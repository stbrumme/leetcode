class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        result = [ 0 ] * n

        # build tree
        next = defaultdict(list)
        for a, b in edges:
            next[a].append(b)
            next[b].append(a)

        # already visited
        seen = set()

        def deeper(node):
            # don't visit twice
            nonlocal seen, result
            if node in seen:
                return None
            seen.add(node)

            have = defaultdict(int)
            for children in next[node]:
                add = deeper(children)
                if add:
                    for a in add:
                        have[a] += add[a]

            # node's label
            current        = labels[node]
            have[current] += 1
            result[node]   = have[current]
            return have

        deeper(0)
        return result
