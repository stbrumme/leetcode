class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x = y = z = 0
        for a, b, c in triplets:
            # consider only triplets where no elements exceeds the target
            if a <= target[0] and b <= target[1] and c <= target[2]:
                # merge them
                x = max(x, a)
                y = max(y, b)
                z = max(z, c)
                # match the target
                if [ x, y, z ] == target:
                    return True

        return False
