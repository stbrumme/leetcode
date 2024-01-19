class Solution:
    def minimumDeletions(self, s: str) -> int:
        # for each position, delete all "b" on its left side and all "a" on its right side
        # finding the optimal position gives us the correct result

        # variable b contains all "b" already seen (left side), variable a all "a" to be discovered (right side)
        a = s.count("a")
        b = 0

        # corner cases: already balanced strings
        if a == 0 or a == len(s):
            return 0

        result = a
        for c in s:
            # update counters
            if c == "a":
                a -= 1
            else:
                b += 1

            # record best split
            result = min(result, a + b)

        return result
