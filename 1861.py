class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        result = []

        # layout of the rotated box
        width  = len(box)
        height = len(box[0])
        for y in range(height):
            result.append([ "." ] * width)

        for x in range(width):
            # rotate
            y2  = width - x - 1

            # next free cell
            pos = height - 1

            for y in reversed(range(height)):
                # rotate
                x2 = y

                # copy obstacle
                if box[y2][x2] == "*":
                    result[y][x] = "*"
                    pos = y - 1

                # drop stone
                if box[y2][x2] == "#":
                    # look for empty cell
                    while result[pos][x] != ".":
                        pos -= 1
                    result[pos][x] = "#"

        return result
