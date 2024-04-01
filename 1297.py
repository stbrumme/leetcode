class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        seen = defaultdict(int)

        left = 0
        freq = defaultdict(int)
        for right, c in enumerate(s):
            # expand
            freq[c] += 1

            # not long enough ?
            size = right - left + 1
            if size < minSize:
                continue

            # respect number of unique letters
            if len(freq) <= maxLetters:
                seen[s[left : right + 1]] += 1

            # shrink
            freq[s[left]] -= 1
            if freq[s[left]] == 0:
                del freq[s[left]]
            left += 1

        return max(seen.values()) if seen else 0
