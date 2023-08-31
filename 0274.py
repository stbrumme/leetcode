class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse = True)
        h = 0
        while h < len(citations) and citations[h] >= h + 1:
            h += 1

        return h
