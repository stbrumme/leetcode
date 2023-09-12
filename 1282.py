class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = defaultdict(set)
        for id, g in enumerate(groupSizes):
            groups[g].add(id)

        result = []
        for g in sorted(groups):
            current = []
            for c in groups[g]:
                current.append(c)
                if len(current) == g:
                    result.append(current)
                    current = []

        return result
