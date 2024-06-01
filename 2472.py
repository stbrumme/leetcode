class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        result = 0
        size   = len(s)

        # good[i] carries a list of start positions of all palindromes with length i
        good = defaultdict(list)
        # every empty string and every string with length 1 is a palindrome
        good[0] = list(range(size))
        good[1] = list(range(size))

        # find all palindromes with 2+ letters
        for i in range(2, size + 1):
            for first in good[i - 2]:
                # idea: xyyx is a palindrome because yy is a palindrome and x == x
                first -= 1
                last   = first + i - 1
                # avoid out of bounds
                if first >= 0 and last < size and s[first] == s[last]:
                    good[i].append(first)

        # transpose good[length][pos] to candidates[pos][length]
        candidates = [ [] for _ in range(size) ]
        for i in range(k, size + 1): # ignore if too short
            for g in good[i]:
                candidates[g].append(i)

        @cache
        def deeper(pos):
            if pos == size:
                return 0

            # skip any palindrome
            best = deeper(pos + 1)
            # iterate over all palindromes at current position
            for c in candidates[pos]:
                best = max(best, 1 + deeper(pos + c))

            return best

        return deeper(0)
