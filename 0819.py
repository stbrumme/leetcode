class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        for c in "!?',;.":
            paragraph = paragraph.replace(c, " ")
        paragraph = paragraph.replace("  ", " ")

        words = defaultdict(int)
        for w in paragraph.split():
            words[w.lower()] += 1

        for b in banned:
            if b.lower() in words:
                del words[b.lower()]

        high = max(words.values())
        for w in words:
            if words[w] == high:
                return w
