class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        # count spells, group by their power
        have = defaultdict(int)
        for p in power:
            have[p] += 1

        power = sorted(have)
        size  = len(power)

        @cache
        def deeper(pos):
            if pos >= size:
                return 0

            current = power[pos]

            # cast current spell, skip next spells
            skip = pos + 1
            while skip < size: # at most two iterations
                if power[skip] > current + 2:
                    break
                skip += 1
            best = have[current] * current + deeper(skip)

            # or skip current spell
            best = max(best, deeper(pos + 1), deeper(pos + 2))

            return best

        return deeper(0)
