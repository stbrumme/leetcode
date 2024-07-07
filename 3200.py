class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        def height(one, two):
            width = 0 # same as height
            while one >= width + 1:
                width += 1
                one   -= width
                one, two = two, one

            return width

        return max(height(red, blue), height(blue, red))
