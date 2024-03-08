class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        height = len(img1)
        width  = len(img1[0])

        # extract ones from second image (to speed up iterating both images over and over again)
        ones = []
        for y in range(height):
            for x in range(width):
                if img2[y][x] == 1:
                    ones.append((x, y))

        # count motion vectors
        motion = [ 0 ] * (width * height * 4) # convert from 2D to 1D for faster array access

        for y in range(height):
            for x in range(width):
                if img1[y][x] == 1:
                    for x2, y2 in ones:
                        # motion vector
                        vx = x2 - x
                        vy = y2 - y
                        id = (vx + width) + (vy + height) * 2 * width
                        motion[id] += 1

        return max(motion)
