class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        width  = len(img[0])
        height = len(img)

        result = []
        for y in range(height):
            result.append([ None ] * width)

        for y in range(height):
            for x in range(width):
                kernel = [ img[y][x] ]
                if x > 0:
                    kernel.append(img[y][x-1])
                if x > 0 and y > 0:
                    kernel.append(img[y-1][x-1])
                if y > 0:
                    kernel.append(img[y-1][x])
                if x < width-1 and y > 0:
                    kernel.append(img[y-1][x+1])
                if x < width-1:
                    kernel.append(img[y][x+1])
                if x < width-1 and y < height-1:
                    kernel.append(img[y+1][x+1])
                if y < height-1:
                    kernel.append(img[y+1][x])
                if y < height-1 and x > 0:
                    kernel.append(img[y+1][x-1])

                result[y][x] = sum(kernel) // len(kernel)

        return result
