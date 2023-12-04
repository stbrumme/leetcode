class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # alien character => english character
        mapping = { x: chr(ord("a") + i) for i, x in enumerate(order) }

        previous = ""
        for w in words:
            # translate
            english = "".join([ mapping[c] for c in w ])
            # compare with most recent word
            if english < previous:
                return False
            previous = english

        return True
