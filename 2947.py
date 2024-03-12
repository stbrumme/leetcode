class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        # brute force
        result = 0

        size = len(s)
        for left in range(size):
            vowels     = 0
            consonants = 0
            for right in range(left, size):
                if s[right] in "aeiou":
                    vowels     += 1
                else:
                    consonants += 1

                if vowels == consonants and (vowels * consonants) % k == 0:
                    result += 1

        return result
