class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ("a", "e", "i", "o", "u")
        have = 0
        for c in s[:k]:
            if c in vowels:
                have += 1

        result = have
        for right in range(k, len(s)):
            left = right - k
            if s[left]  in vowels:
                have -= 1
            if s[right] in vowels:
                have += 1

            result = max(result, have)

        return result
