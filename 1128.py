class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        result = 0

        have = defaultdict(int)
        for a, b in dominoes:
            # ensure a <= b
            key = (min(a, b), max(a, b))
            result    += have[key]
            have[key] += 1

        return result
