class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        @cache
        def x(a, b):
            if a == b:
                return arr[a]
            else:
                return arr[a] ^ x(a + 1, b)

        result = 0
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                for k in range(j, len(arr)):
                    if x(i, j - 1) == x(j, k):
                        result += 1

        return result
