class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        sections = 12
        # iterate over all 2^11 bitmasks, ignore section 0
        # if a bit is 1, then Bob tries to score one more arrow than Alice
        candidates = defaultdict(list)
        for bits in range(0, 1 << sections, 2):
            score = 0
            need  = 0 # arrows needed
            for i in range(1, sections):
                if (1 << i) & bits:
                    score += i
                    need  += aliceArrows[i] + 1
                    if need > numArrows:
                        break

            # accept only if enough arrows
            if need <= numArrows:
                candidates[score].append(bits)

        # pick first valid candidate
        for score in sorted(candidates, reverse = True):
            for bits in candidates[score]:
                result = [ 0 ] * sections
                for i in range(1, sections):
                    if (1 << i) & bits:
                        result[i] = aliceArrows[i] + 1

                # throw unused arrows at section 11
                result[-1] += numArrows - sum(result)
                return result

        # zero score, all arrows in section 0
        return [ numArrows ] + [ 0 ] * (sections - 1)
