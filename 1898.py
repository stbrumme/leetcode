class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def impossible(k):
            # relevant indices
            remove = sorted(removable[ : k])

            b = 0 # index for p
            r = 0 # index for remove
            for a in range(len(s)):
                if r < len(remove) and remove[r] == a:
                    # skip
                    r += 1
                else:
                    # try to extend subsequence
                    if s[a] == p[b]:
                        b += 1
                        if b == len(p):
                            # full subsequence found, it's possible => not impossible
                            return False

            return True # failed to build subsequence

        return bisect_left(range(len(removable) + 1), True, key = impossible) - 1
