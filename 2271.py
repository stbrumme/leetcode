class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        # carpet should start at the same position where some white tiles start
        result = 0

        tiles.sort()
        size = len(tiles)

        covered = 0 # groups of white tiles completely covered
        right   = 0 # "left" and "right" are tile IDs
        for left in range(size):
            last = tiles[left][0] + carpetLen - 1 # end of carpet

            # grow our sliding window
            while right < size and tiles[right][1] <= last:
                start, end = tiles[right]
                covered   += 1 + end - start
                right     += 1

            # last group of tiles may be partially covered
            partially = 0
            if right < size:
                start, end = tiles[right]
                if start <= last:
                    partially = 1 + last - start

            result = max(result, covered + partially)

            # early exit
            if result == carpetLen or right == size:
                break

            # shrink extent sliding window
            start, end = tiles[left]
            covered   -= 1 + end - start

        return result
