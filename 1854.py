class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        result = 0

        # determine delta per year
        changes = defaultdict(int)
        for birth, death in logs:
            changes[birth] += 1
            changes[death] -= 1

        have = 0
        high = 0
        for year in sorted(changes):
            delta = changes[year]
            have += delta
            # higher than before ?
            if high < have:
                high   = have
                result = year

        return result
