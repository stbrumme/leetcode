class Solution:
    def reorderSpaces(self, text: str) -> str:
        # extract words
        words  = []
        for w in text.split(" "):
            if w != "":
                words.append(w)

        spaces = text.count(" ")
        gaps   = len(words) - 1                    # number of gaps between words
        insert = spaces // gaps if gaps > 0 else 0 # number of spaces for each gap
        final  = spaces - insert * gaps            # number of spaces at the end

        return (" " * insert).join(words) + " " * final
