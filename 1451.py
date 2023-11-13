class Solution:
    def arrangeWords(self, text: str) -> str:
        words = text.lower().split()
        words.sort(key = lambda w : len(w)) # Python has stable sort
        words[0] = words[0].title()
        return " ".join(words)
