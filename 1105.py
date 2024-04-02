class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        @cache
        def deeper(pos, width, height): # width and height refer to the current row only
            # last row
            if pos == len(books):
                return height

            w, h = books[pos]

            # start new row
            best = height + deeper(pos + 1, w, h)
            # try to add to previous row (if enough space available)
            if width + w <= shelfWidth:
                best = min(best, deeper(pos + 1, width + w, max(h, height)))
            return best

        return deeper(0, 0, 0)
