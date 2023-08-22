class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True

        flowerbed = [0] + flowerbed + [0]

        spots = 0
        for i in range(2, len(flowerbed)):
            if flowerbed[i - 2] == 0 and flowerbed[i - 1] == 0 and flowerbed[i] == 0:
                spots += 1
                if spots == n:
                    return True
                flowerbed[i - 1] = 1

        return False
