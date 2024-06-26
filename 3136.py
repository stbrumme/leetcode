class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False

        v = 0 # counter for vowels
        c = 0 # counter for consonants

        allowed = "0123456789abcdefghijklmnopqrstuvwxyz"
        digits  = "0123456789"
        vowels  = "aeiou"
        for w in word:
            # invalid
            if w.lower() not in allowed:
                return False

            if w in digits:
                continue
            if w.lower() in vowels:
                v += 1
            else:
                c += 1

        return v * c > 0
