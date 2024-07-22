class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = "aeiou"
        total  = sum(s.count(v) for v in vowels)

        if total == 0:
            return False

        # case 1: Alive begins, removes the whole string and wins
        # case 2: Alice removes all but one vowel
        # case 2a: no consonants left => Alice wins
        # case 2b: something's left => Bob takes it
        #          and then Alice proceed as in case 1 and wins
        return True
