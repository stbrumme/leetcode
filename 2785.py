class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = set([ "A", "E", "I", "O", "U", "a", "e", "i", "o", "u" ])
        # extract vowels in sorted order
        v = sorted([ c for c in s if c in vowels ])
        used = 0

        # strings are immutable, let's use lists
        result = []
        for c in s:
            if c in vowels:
                # replace vowel
                result.append(v[used])
                used += 1
            else:
                # keep consonant
                result.append(c)

        # convert to string
        return "".join(result)
