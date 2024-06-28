class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        result = 0

        height = len(mat)
        width  = len(mat[0])
        limit  = min(width, height) # maximum side length

        # 2D prefix sum
        @cache
        def deeper(x, y):
            if x < 0 or y < 0:
                return 0

            # suppose we have an area: ab
            #                          cd
            # then d = value + b + c - a
            return mat[y][x] + deeper(x - 1, y) + deeper(x, y - 1) - deeper(x - 1, y - 1)

        # try every possible upper-left corner
        for y in range(height):
            for x in range(width):
                for s in range(max(0, result - 1), limit):
                    # lower-right corner
                    x2 = x + s
                    y2 = y + s

                    # out of bounds
                    if x2 >= width or y2 >= height:
                        break

                    # suppose we need the square at d: ab
                    #                                  cd
                    # then d = prefix[d] - prefix[b] - prefix[c] + prefix[a]
                    total = deeper(x2, y2) + deeper(x - 1, y - 1) - deeper(x - 1, y2) - deeper(x2, y - 1)
                    if total > threshold:
                        break

                    result = s + 1

        return result
