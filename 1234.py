class Solution:
    def balancedString(self, s: str) -> int:
        result   = size = len(s)
        expected = size // 4 # how often Q, W, E and R should be found (if balanced)

        # fun fact regarding the ASCII codes of Q, W, E, R:
        # if we ignore the lowest bit, then the next two lowest bits are Q => 00, W => 11, E => 10, R => 01
        # that's perfect for indexing a simple array !
        index = lambda x : (ord(x) >> 1) & 3
        #        Q  R  E  W
        freq = [ 0, 0, 0, 0 ]
        for c in s:
            freq[index(c)] += 1

        # yet another sliding window
        left = 0
        for right, c in enumerate(s):
            freq[index(c)] -= 1 # enlarge substring

            # if still balanced, then shrink substring
            while left < size and max(freq) <= expected:
                result = min(result, right - left + 1)
                freq[index(s[left])] += 1
                left += 1

        return result
