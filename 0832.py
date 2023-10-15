class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for y in range(len(image)):
            for x in range(len(image[y])):
                image[y][x] ^= 1
            image[y] = reversed(image[y])
        return image
