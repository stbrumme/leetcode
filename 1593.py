class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def deeper(start, have):
            if start == len(s):
                print(have)
                return 0

            best = 0
            for end in range(start + 1, len(s) + 1): # point beyond last element
                sub = s[start : end]
                if sub in have:
                    continue

                have.add(sub)
                best = max(best, 1 + deeper(end, have))
                have.discard(sub) # allows re-using this set() again

            return best

        return deeper(0, set())
