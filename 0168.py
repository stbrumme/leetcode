class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        # careful: 1-based numeration scheme
        while columnNumber > 0:
            result = chr(ord("A") + (columnNumber - 1) % 26) + result
            columnNumber = (columnNumber - 1) // 26
        return result
