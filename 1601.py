class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        size = len(requests)

        result = 0
        for i in range(2**size):
            mask = bin(i)[2:].zfill(size)
            num = mask.count("1")
            if num <= result:
                continue

            buildings = [0] * n
            for pos, consider in enumerate(mask):
                if consider == "1":
                    leave, enter = requests[pos]
                    buildings[leave] -= 1
                    buildings[enter] += 1

            if max(buildings) == 0:
                result = num

        return result
