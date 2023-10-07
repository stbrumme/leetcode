class Solution:
    def minCut(self, s: str) -> int:
        cache = {}
        keyshift = 10_000 # or len(s)

        def isPalindrome(left, right):
            # simple adding @cache causes use of too much memory
            # let's build a caching scheme on our own
            key = left * keyshift + right
            if key in cache:
                return cache[key]

            if left >= right: # one or zero letters
                result = True
            elif s[left] != s[right]:
                result = False
            else:
                result = isPalindrome(left + 1, right - 1)

            cache[key] = result
            return result

        cuts = [ 9999999 ] * len(s) # cuts before index i
        for left in range(len(s)):
            for right in range(left, len(s)):
                if isPalindrome(left, right):
                    if left == 0:
                        cuts[right] = 0 # left border, no cut needed
                    else:
                        cuts[right] = min(cuts[right], cuts[left - 1] + 1)

        return cuts[-1]
