class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diffs = []
        for i, (c1, c2) in enumerate(zip(s1, s2)):
            if c1 != c2:
                diffs.append(i)

        # exactly two or no differences
        if not diffs:
            return True
        if len(diffs) != 2:
            return False

        # make sure the swapped letters are identical
        return s1[diffs[0]] == s2[diffs[1]] and s1[diffs[1]] == s2[diffs[0]]
