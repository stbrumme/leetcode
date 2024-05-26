class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        # trivial case
        if rows == 1:
            return encodedText

        result = ""
        height = rows
        width  = ceil(len(encodedText) / rows)

        startx = x = y = 0
        while x < width:
            i       = y * width + x
            result += encodedText[i]

            x += 1
            y += 1
            if y == height:
                startx += 1
                x = startx
                y = 0

        return result.rstrip()
