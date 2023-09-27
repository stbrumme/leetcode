class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        all = set(ideas) # faster lookups

        # split (first letter => remainder)
        prefix = defaultdict(set)
        for name in ideas:
            prefix[name[0]].add(name[1:])

        result = 0
        for p1 in sorted(prefix):
            for p2 in sorted(prefix):
                if p1 != p2: # must be different first letter
                    result += len(prefix[p1] - prefix[p2]) * len(prefix[p2] - prefix[p1])

        return result
