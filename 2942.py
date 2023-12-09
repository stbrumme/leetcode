class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        for i, w in enumerate(words):
            if w.find(x) >= 0:
                yield i
