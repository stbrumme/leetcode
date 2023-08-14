class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = {
                "q": 1, "w": 1, "e": 1, "r": 1, "t": 1, "y": 1, "u": 1, "i": 1, "o": 1, "p": 1,
                "a": 2, "s": 2, "d": 2, "f": 2, "g": 2, "h": 2, "j": 2, "k": 2, "l": 2,
                "z": 4, "x": 4, "c": 4, "v": 4, "b": 4, "n": 4, "m": 4 }

        result = []
        for w in words:
            mask = 0
            for c in w.lower():
                mask |= rows[c]
            if mask in [ 1, 2, 4 ]:
                result.append(w)

        return result
