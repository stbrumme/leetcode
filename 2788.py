class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        for w in words:
            yield from [ text for text in w.split(separator) if text ]
