class Solution:
    def resultGrid(self, image: List[List[int]], threshold: int) -> List[List[int]]:
        height = len(image)
        width  = len(image[0])

        # return average intensity or None if exceeding threshold or invalid
        @lru_cache(maxsize = 500 * 3)
        def region(x, y):
            # reject out-of-bounds
            if not (1 <= x < width  - 1):
                return None
            if not (1 <= y < height - 1):
                return None

            # check threshold
            for delta in range(-1, +1 + 1):
                imx = image[y][x + delta]
                imy = image[y + delta][x]

                if abs(image[y - 1][x + delta] - imx) > threshold:
                    return None
                if abs(image[y + 1][x + delta] - imx) > threshold:
                    return None
                if abs(image[y + delta][x - 1] - imy) > threshold:
                    return None
                if abs(image[y + delta][x + 1] - imy) > threshold:
                    return None

            # average
            avg = 0
            for dy in range(y - 1, y + 1 + 1):
                for dx in range(x - 1, x + 1 + 1):
                    avg += image[dy][dx]
            return avg // 9 # round down

        result = [ [ 0 ] * width for _ in range(height) ]
        for y in range(height):
            for x in range(width):
                total = 0
                size  = 0
                for dy in range(y - 1, y + 1 + 1):
                    for dx in range(x - 1, x + 1 + 1):
                        r = region(dx, dy)
                        # exclude 3x3 subgrids which are no true regions
                        # (either partially outside or above threshold)
                        if r is not None:
                            total += r
                            size  += 1

                if   size == 0:
                    result[y][x] = image[y][x]   # plain copy
                elif size == 1:
                    result[y][x] = total         # just one valid region
                else:
                    result[y][x] = total // size # rounded down average

        return result
