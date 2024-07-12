class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        result = 0

        # keep letters on the right side,
        # swap letters on the left  side into position

        pairs = len(s) // 2
        for i in range(pairs):
            # match last letter
            last  = s[-1]
            s     = s[ : -1]

            other = s.find(last)

            if other >= 0:
                # remove it
                s = s[ : other] + s[other + 1 : ]
                result += other
            else:
                # odd length: middle letter has no partner
                result += len(s) // 2

        return result
