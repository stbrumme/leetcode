class Solution:
    def capitalizeTitle(self, title: str) -> str:
        words = []
        for w in title.split(" "):
            if len(w) > 2:
                words.append(w.capitalize())
            else:
                words.append(w.lower())

        return " ".join(words)
