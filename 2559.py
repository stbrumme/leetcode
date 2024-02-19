class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        # sorted indices of "vowel words"
        vowels = [ i for i, w in enumerate(words) if w[0] in "aeiou" and w[-1] in "aeiou" ]

        # process ranges
        for l, r in queries:
            left  = bisect_left(vowels, l)
            right = bisect_left(vowels, r + 1)
            yield right - left
